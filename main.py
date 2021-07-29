
import sys, os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

## ==> SESSION WINDOW
from ui_session_screen import Ui_SessionWindow

##==> FINAL WINDOW
from ui_endstat_screen import Ui_EndResultWindow

##==> ERROR WINDOW
from ui_error_screen import Ui_ErrorWindow

##==> AUTH WINDOW
from ui_auth_page import Ui_AuthWindow,loadAuthPage,checkAuthPage

##==> LICENSE WINDOW
from ui_license_page import Ui_LicenseWindow

##== > DATABASE IMPORT
from database import DiscordData,LocalData,Database

## ==> BOT IMPORTS
import time
import pyautogui as pag
from datetime import datetime, timedelta
import win32api
import pytesseract
import random
import keyboard
import asyncio
from PIL import Image
import requests
import json
import subprocess
from collections import namedtuple
from gameinput import KeyPress

#COMPILE FUNCTION
def popen(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return process.stdout.read()

def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

## ==> GLOBALS
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
counter = 0
game_counter = 0
games_list = []
is_first = True
game_start_time = 0.00
game_time_stamp = datetime.now()

OAUTH2_REDIRECT = #YOUR GENERATED OAUTH2 REDIRECT 
API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = #YOUR CLIENT ID HERE [DISCORD]
CLIENT_SECRET = #YOUR CLIENT SECERET HERE [DISCORD]
REDIRECT_URI = 'https://discord.com/channels/@me'

L_K = str()

hwid = str(popen("wmic csproduct get UUID")).strip().replace(r"\r", "").split(r"\n")[1].strip()

res = namedtuple('res',['x','y','startRegion','startClick','playAgainRegion','playAgainClick','inGameRegion'])
res.x = (1920)
res.y = (1080)
res.startRegion = (900, 890, 72, 50)
res.startClick = (938,895)
res.playAgainRegion = (870, 933, 137, 33)
res.playAgainClick = (932,948)
res.inGameRegion = (1663, 952, 60, 20)

def incrementCounter():
    global game_counter
    game_counter += 1
    return game_counter

def appendGameList():
    global games_list,game_time_stamp
    game_end_time = time.time()
    games_list.append(["Game {}".format(len(games_list)+1),
        "{}/{}".format(game_time_stamp.day,game_time_stamp.month),
        datetime.strptime("{}:{}".format(game_time_stamp.hour,game_time_stamp.minute),"%H:%M").strftime("%I:%M %p"),
        str(timedelta(seconds=(game_end_time-game_start_time))).split('.')[0]])

def set_LK(key):
    global L_K
    L_K = key

def file_check():
    if os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
        if os.path.exists(r"C:\images\is_dm.png"):
            if os.path.exists(r"C:\images\not_dm.png"):
                return True
            else:
                error = ErrorWindow()
                error.raiseError("FileNotFoundError [{}]".format("C:/images/not_dm.png"))
                error.show()
        else:
            error = ErrorWindow()
            error.raiseError("FileNotFoundError [{}]".format("C:/images/is_dm.png"))
            error.show()
    else:
        error = ErrorWindow()
        error.raiseError("{}".format('Tesseract-OCR PATH not found'))
        error.show()
    return False


# ERROR SCREEN
class ErrorWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ErrorWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.closeButton.clicked.connect(lambda : self.close())

        self.oldPos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def raiseError(self,error):
        self.ui.label_errorInfo.setText(error)

# END RESULT SCREEN
class EndResultWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_EndResultWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.stat()

        self.ui.closeButton.clicked.connect(lambda : self.close())

        self.oldPos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def stat(self):
        self.ui.statTable.setRowCount(len(games_list))
        self.ui.statTable.setVerticalHeaderLabels([games[0] for games in games_list])
        self.ui.label_total_xp.setText("<strong>Gained</strong> {}xp ".format(len(games_list)*900))
        game_row = 0
        for games in games_list:
            game_col = 0
            for data in games[1:]:
                cell = QTableWidgetItem(data)
                self.ui.statTable.setItem(game_row,game_col,cell)
                game_col += 1
            game_row += 1
            
# STATUS SCREEN
class SessionWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SessionWindow()
        self.ui.setupUi(self)

        # WINDOWLESS UI
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # BUTTON FUNCTIONS
        self.ui.closeButton.clicked.connect(lambda : self.closeAll())
        self.ui.endtask.clicked.connect(lambda : self.finalWindow())

        self.botThread = ValorantBot()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.countdown)

        self.timer.start(1000)
        self.start_countdown = 6

        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_status.setText("<strong>STARTING IN {}</strong>".format(5)))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_status.setText("<strong>STARTING IN {}</strong>".format(4)))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_status.setText("<strong>STARTING IN {}</strong>".format(3)))
        QtCore.QTimer.singleShot(4000, lambda: self.ui.label_status.setText("<strong>STARTING IN {}</strong>".format(2)))
        QtCore.QTimer.singleShot(5000, lambda: self.ui.label_status.setText("<strong>STARTING IN {}</strong>".format(1)))

        ## UPDATE STATUS AND GAME COUNT
        self.botThread.current_status.connect(self.setStatus)
        self.botThread.game_count.connect(self.gameCount)

        self.oldPos = self.pos()

    def countdown(self):
        if self.start_countdown == 0:
            self.timer.stop()
            self.botThread.start()
        
        self.start_countdown -= 1

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def setStatus(self, current_status):
        self.ui.label_status.setText("<strong>Status </strong> : {}".format(current_status))

    def gameCount(self, game_count):
        self.ui.label_game_count.setText("<strong>Game Count </strong> : {}".format(game_count))

    def finalWindow(self):
        self.botThread._quit()
        self.botThread.quit()
        if len(games_list) > 0:
            self.finalWindow_ = EndResultWindow()
            self.finalWindow_.show()
        self.close()

    def closeAll(self):
        self.botThread._quit()
        self.botThread.quit()
        self.close()

# OPTION MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.farmButton.clicked.connect(lambda: self.setChoice(0))
        self.ui.afkButton.clicked.connect(lambda : self.setChoice(1))
        self.ui.closeButton.clicked.connect(lambda : self.close())
        self.ui.Start.clicked.connect(lambda : self.session())
        self.ui.radio_1080p.clicked.connect(lambda : self.resolution(0))
        self.ui.radio_1440p.clicked.connect(lambda : self.resolution(1))
        self.ui.radio_4k.clicked.connect(lambda : self.resolution(2))
        self.scrn_size = pag.size()
        self.ui.label_rec_res.setText("Recommended  : {}x{}".format(self.scrn_size.width,self.scrn_size.height))

        self.oldPos = self.pos()

        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def resolution(self,user_res):
        global res
        if user_res == 0:
            res.x = (1920)
            res.y = (1080)
            res.startRegion = (900, 890, 72, 50)
            res.startClick = [938,895]
            res.playAgainRegion = (870, 933, 137, 33)
            res.playAgainClick = (932,948)
            res.inGameRegion = (1663, 952, 60, 20)
        if user_res == 1:
            res.x = (2560)
            res.y = (1440)
            res.startRegion = (1207,1148,85,32)
            res.startClick = [1243,1163]
            res.playAgainRegion = (1176,1187,151,30)
            res.playAgainClick = (1250,1202)
            res.inGameRegion = (2132,1211,58,21)
        if user_res == 2:
            res.x = (1920*2)
            res.y = (1080*2)
            res.startRegion = (900*2, 890*2, 72*2, 50*2)
            res.startClick = [938*2,895*2]
            res.playAgainRegion = (870*2, 933*2, 137*2, 33*2)
            res.playAgainClick = (1250*2,1202*2)
            res.inGameRegion = (1663*2, 952*2, 60*2, 20*2)

    def setChoice(self,x):
        if x == 0:
            self.ui.Start.setText("Start XP Farm Bot")
        if x == 1:
            self.ui.Start.setText("Start AFK Bot")

    def session(self): 
        #switch to session tab to show status
        if self.ui.Start.text() in "Start XP Farm Bot":
            self.session_ = SessionWindow()
            self.session_.show()

        elif self.ui.Start.text() in "Start AFK Bot":
            pass
        else:
            self.session_ = SessionWindow()
            self.session_.show()

        self.close()

# DISCORD AUTH
class AuthWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #AUTHORIZATION
        self.auth_view = loadAuthPage()
        self.auth_view.setUrl(QUrl(OAUTH2_REDIRECT))
        self.ui.horizontalLayout.addWidget(self.auth_view)
        self.check_auth = checkAuthPage(self.auth_view,self)
        self.ui.closeButton.clicked.connect(lambda : self.closeAll())
        self.check_auth.start()
        self.check_auth.bearer_code.connect(self.set_code)

    def set_code(self,code):
        self.closeAll()
        self.code = str(code)
        self.get_userdata(self.code)
        return

    def get_userdata(self, code):
        self._userdata = DiscordData()
        self._token : Final = self._userdata.exchange_code(code)
        self._data : Final = self._userdata.exchange_userdata(self._token['access_token'])
        self.setup_user(self._token, self._data)
        return

    def setup_user(self, token,data):
        self.token = token
        self.data = data
        self.local_data = LocalData()
        self.data_base = Database()
        write_to_userdata = {'_id': self.data['id'],
                             'username': self.data['username'],
                             'discriminator': self.data['discriminator'],
                             'key': L_K,
                             'HWID': hwid,
                             'access_token': self.token['access_token'],
                             'refresh_token': self.token['refresh_token'],
                             'time_stamp' : str(datetime.now())
                             }
        self.local_data.setConfig(write_to_userdata)
        self.data_base.add_users(self.data,hwid,L_K)
        self.data_base.pop_key(L_K)
        self.main_window = MainWindow()
        self.main_window.show()

    def closeAll(self):
        print('closing page')
        self.check_auth._stop()
        time.sleep(.5)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# LICENSE AUTH
class LicenseWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LicenseWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.closeButton.clicked.connect(lambda : self.close())
        self.ui.check_button.clicked.connect(lambda : self.validate_key())


    def validate_key(self):
        self.data_base = Database()
        temp_key = str(self.ui.lineEdit.text())
        if self.data_base.check_key(temp_key):
            set_LK(temp_key)
            self.auth_window = AuthWindow()
            self.auth_window.show()
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(30)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APP")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            
            self.timer.stop()
            self.local_data = LocalData()
            self.data_base = Database()
            self.pass_check = False
            # check if config is valid
            if self.local_data.check_config():
                user_data = self.local_data.getConfig()
                if self.data_base.check_user(user_data,hwid):
                        self.pass_check = True


            if self.pass_check:
                if file_check():
                    self.main = MainWindow()
                    self.main.show()
            else:
                self.license = LicenseWindow()
                self.license.show()

            self.close()

        # INCREASE COUNTER
        counter += 1

# BOT QTHREAD
class ValorantBot(QThread):
    current_status = Signal(str)
    game_count = Signal(int)

    def __init__(self):
        QThread.__init__(self)   
        self.DM_SCREEN = Image.open(r"C:\images\is_dm.png")
        self.NOT_DM_SCREEN = Image.open(r"C:\images\not_dm.png")
        self.CONFIDENCE = 0.65
        self.loop_stat = True
        self.DM_IS_SET = False
       
    async def _deathmatch(self):
        IS_NOT_DM_SCREEN = pag.locateCenterOnScreen(self.NOT_DM_SCREEN, confidence=0.81)
        IS_DM_SCREEN = pag.locateCenterOnScreen(self.DM_SCREEN, confidence=0.81)

        if IS_NOT_DM_SCREEN is not None and IS_DM_SCREEN is None:
            self.current_status.emit("setting up...")
            self.click(IS_NOT_DM_SCREEN.x, IS_NOT_DM_SCREEN.y)
            self.DM_IS_SET = True
            win32api.SetCursorPos((res.x // 2, res.y // 2))
        elif IS_DM_SCREEN is not None:
            self.DM_IS_SET = True
        
    async def _startgame(self):
        is_start_button = pag.screenshot(r"C:\images\start_button.png", region=res.startRegion)
        is_start_button = str(pytesseract.image_to_string(is_start_button, config= r'--oem 3 --psm 6'))
        if 'START' in is_start_button and self.DM_IS_SET:
            self.current_status.emit("queuing...")
            self.click(res.startClick[0],res.startClick[1])
            win32api.SetCursorPos((res.x // 2, res.y // 2))

    async def _playagain(self):
        global is_first
        is_play_again = pag.screenshot(r"C:\images\play_again.png", region=res.playAgainRegion)
        is_play_again = str(pytesseract.image_to_string(is_play_again, config= r'--oem 3 --psm 6'))
        if 'PLAY AGAIN' in is_play_again:
            self.current_status.emit("requeuing...")
            self.click(res.playAgainClick[0],res.playAgainClick[1])
            win32api.SetCursorPos((res.x // 2, res.y // 2))
            appendGameList()
            is_first = True

    async def _ingame(self):
        global game_start_time,is_first,game_time_stamp
        in_game = pag.screenshot(r"C:\images\in_game.png", region=res.inGameRegion)
        is_in_game = str(pytesseract.image_to_string(in_game, config=r'--oem 3 --psm 6'))
        if '12,000' in is_in_game or len(is_in_game) > 4:
            if is_first:
                self.current_status.emit("in game...")
                game_start_time = time.time()
                game_time_stamp = datetime.now()
                self.game_count.emit(incrementCounter())
                is_first = False
            dur = random.uniform(0.3,1)
            keyboard_keys = [0x11, 0x1E, 0x1F, 0x20, 0x03, 0x04]
            if random.randint(0,1) == 1:
                KeyPress(keyboard_keys[random.randint(0,5)])
            else:
                pag.click()
            await asyncio.sleep(dur)

    def click(self,x, y):
        win32api.SetCursorPos((x, y))
        pag.click(button='left', duration=0.3)  
             
    async def task(self):
        await asyncio.gather(
            self._deathmatch(),
            self._startgame(),
            self._playagain(),
            self._ingame())

    def run(self):
        while self.loop_stat:
            asyncio.run(self.task())
            if keyboard.is_pressed('q'):
                self.current_status.emit("STOPPED")
                self._quit()

    def _quit(self):
        self.loop_stat = False
        self.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

