from pymongo import MongoClient
import os, sys
import requests
import json
import datetime

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = #YOUR CLIENT ID HERE
CLIENT_SECRET = #YOUR CLIENT SECERET HERE
REDIRECT_URI = 'https://discord.com/channels/@me'
MONGO_DB_USERNAME = #YOUR USERNAME HERE
MONGO_DB_PASSWORD = #YOUR PASSWORD HERE

class DiscordData():

    def exchange_code(self, code):
        data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
        # r.raise_for_status()
        return r.json()

    def exchange_userdata(self, token):
        self.user_data = requests.get("%s/users/@me" % API_ENDPOINT,
                                      headers={'Authorization': 'Bearer %s' % token})
        return self.user_data.json()

    def exchange_refresh_token(self, r_token):
        data = {
            'client_id' : CLIENT_ID,
            'client_secret' : CLIENT_SECRET,
            'grant_type' : 'refresh_token',
            'refresh_token' : r_token,
        }
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded'
        }
        response = requests.post('%s/oauth2/token'%API_ENDPOINT, data=data, headers=headers)
        return response.json()


class LocalData:
    def __init__(self):
        self.user_data_path = 'C:/Users/%s/AppData/Roaming/Frux-Bot/config' % os.getlogin()
        self.check_path()

    def check_path(self):
        if os.path.exists(self.user_data_path):
            pass
        else:
            parent_dir = 'C:/Users/%s/AppData/Roaming' % os.getlogin()
            os.mkdir(os.path.join(parent_dir, 'Frux-Bot'), 0o666)
            os.mkdir(os.path.join(parent_dir, 'Frux-Bot', 'config'), 0o666)

    def check_config(self):
        return os.path.exists(os.path.join(self.user_data_path, 'creds.json'))

    def setConfig(self, data):
        data.pop('HWID')
        with open(os.path.join(self.user_data_path, 'creds.json'), 'w+') as creds:
            json.dump(data, creds)

    def getConfig(self):
        with open(os.path.join(self.user_data_path, 'creds.json'), 'r') as creds:
            return json.load(creds)
        return None


class Database:
    def __init__(self):
        self.username = MONGO_DB_USERNAME
        self.password = MONGO_DB_PASSWORD
        self.uri = 'mongodb+srv://{}:{}@cluster0.jgocs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'.format(
            self.username, self.password)
        self.cluster = MongoClient(self.uri)

    def add_users(self, user_dict: dict, hwid: str, key: str):
        db = self.cluster["users"]
        collection = db["authorized_users"]
        data = {'_id': user_dict['id'],
                'username': user_dict['username'],
                'discriminator': user_dict['discriminator'],
                'activated_key': key,
                'HWID': hwid,
                }
        collection.insert_one(data)

    def check_user(self, user_dict: dict, hwid: str):
        db = self.cluster["users"]
        collection = db["authorized_users"]
        difference = datetime.datetime.now() - datetime.datetime.strptime(user_dict['time_stamp'], '%Y-%m-%d %H:%M:%S.%f')
        if difference.total_seconds() < 604800:
            user_dict_local = user_dict
            user_dict = DiscordData().exchange_userdata(user_dict['access_token'])
            data = {'_id': user_dict['id'],
                    'username': user_dict['username'],
                    'discriminator': user_dict['discriminator'],
                    'activated_key': user_dict_local['key'],
                    'HWID': hwid,
                    }
            if collection.find_one(data) is not None:
                return True
        else:
            new_user_token_data = DiscordData().exchange_refresh_token(user_dict['refresh_token'])
            print(new_user_token_data)
            new_user_data = DiscordData().exchange_code(new_user_token_data['access_token'])
            old_user_data = LocalData().getConfig()
            data = {'_id': new_user_data['id'],
                    'username': new_user_data['username'],
                    'discriminator': new_user_data['discriminator'],
                    'activated_key': old_user_data['activated_key'],
                    'HWID': hwid
                    }
            if collection.find_one(data) is not None:
                LocalData().setConfig({'_id' : new_user_data['_id'],
                                       'username' : new_user_data['username'],
                                       'discriminator' : new_user_data['username'],
                                       'key' : old_user_data['activated_key'],
                                       'access_token' : new_user_token_data['access_token'],
                                       'refresh_token' : new_user_token_data['refresh_token'],
                                       'time_stamp' : str(datetime.datetime.now())})
                return True
        return False

    def remove_user(self, _id):
        self.db = self.cluster["users"]
        self.collection = self.db["authorized_users"]
        self.collection.delete_one({"_id": _id})

    def check_key(self, key: str):
        self.db = self.cluster["license_keys"]
        self.collection = self.db["available_keys"]
        if self.collection.find_one({'license_key': key}) is not None:
            return True
        return False

    def pop_key(self, key: str):
        self.db = self.cluster["license_keys"]
        self.collection = self.db["available_keys"]
        self.collection.delete_one({'license_key': key})
