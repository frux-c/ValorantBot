import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QThread, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView
import time


class loadAuthPage(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.page = QWebEngineView()


class checkAuthPage(QThread):
    bearer_code = Signal(str)

    def __init__(self, page, window):
        QThread.__init__(self)
        self.code = str()
        self.page = page
        self.window = window
        self.loop_state = True

    @property
    def auth_code(self):
        if self.code == '':
            return None
        return self.code

    def _stop(self):
        self.loop_state = False
        self.quit()
        self.window.close()

    def run(self):
        while self.loop_state:
            time.sleep(0.5)
            if 'https://discord.com/channels/@me' in self.page.url().toString():
                self.code = self.page.url().toString().split('?')[-1].replace('code=', '')
                self.bearer_code.emit(self.code)
                return;


class Ui_AuthWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(580, 680)
        MainWindow.setStyleSheet("QFrame {    \n"
                                 "    background-color: rgb(56, 58, 89);    \n"
                                 "    color: rgb(220, 220, 220);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setStyleSheet("color : rgb(98, 114, 164);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close_frame = QFrame(self.frame)
        self.close_frame.setMaximumSize(QtCore.QSize(16777215, 20))
        self.close_frame.setFrameShape(QFrame.StyledPanel)
        self.close_frame.setFrameShadow(QFrame.Raised)
        self.close_frame.setObjectName("close_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.close_frame)
        self.horizontalLayout_2.setContentsMargins(510, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.closeButton = QPushButton(self.close_frame)
        self.closeButton.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.closeButton.setStyleSheet(".QPushButton {\n"
                                       "    background-color:transparent;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    padding:16px 31px;\n"
                                       "    text-decoration:none;\n"
                                       "    text-align:center;\n"
                                       "    vertical-align: middle;\n"
                                       "}\n"
                                       "\n"
                                       ".QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(255, 0, 0);\n"
                                       "    border-radius:8px;\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.closeButton.setCheckable(False)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout_2.addWidget(self.close_frame)
        self.label_title = QLabel(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.browser_frame = QFrame(self.frame)
        self.browser_frame.setFrameShape(QFrame.StyledPanel)
        self.browser_frame.setFrameShadow(QFrame.Raised)
        self.browser_frame.setObjectName("browser_frame")
        self.horizontalLayout = QHBoxLayout(self.browser_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.addWidget(self.browser_frame)
        self.label = QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label.setFont(font)
        self.label.setStyleSheet("    color: rgb(98, 114, 164);")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.label_title.setText(_translate("MainWindow", "<strong>Frux\'s</strong> BOT"))
        self.label.setText(_translate("MainWindow", "©COPYRIGHT, FRUXC"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_AuthWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
