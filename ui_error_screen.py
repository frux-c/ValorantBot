# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys, os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QThread, Signal)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import * 

class Ui_ErrorWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(680, 400)
        MainWindow.setMinimumSize(QSize(680, 400))
        MainWindow.setMaximumSize(QSize(680, 400))
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(610, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QPushButton(self.frame_2)
        self.closeButton.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setFamily("Small Fonts")
        font.setBold(False)
        font.setWeight(50)
        self.closeButton.setFont(font)
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
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.label_title = QLabel(self.frame)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.label_error = QLabel(self.frame)
        self.label_error.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color : rgb(98, 114, 164);")
        self.label_error.setAlignment(Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.verticalLayout_2.addWidget(self.label_error)
        self.label_errorInfo = QLabel(self.frame)
        font = QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.label_errorInfo.setFont(font)
        self.label_errorInfo.setStyleSheet("color : rgb(98, 114, 164);")
        self.label_errorInfo.setAlignment(Qt.AlignCenter)
        self.label_errorInfo.setObjectName("label_errorInfo")
        self.verticalLayout_2.addWidget(self.label_errorInfo)
        self.label_contact = QLabel(self.frame)
        self.label_contact.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_contact.setFont(font)
        self.label_contact.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_contact.setAlignment(Qt.AlignCenter)
        self.label_contact.setObjectName("label_contact")
        self.verticalLayout_2.addWidget(self.label_contact)
        self.label_copyright = QLabel(self.frame)
        self.label_copyright.setMaximumSize(QSize(16777215, 15))
        self.label_copyright.setStyleSheet("    color: rgb(98, 114, 164);")
        self.label_copyright.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_copyright.setObjectName("label_copyright")
        self.verticalLayout_2.addWidget(self.label_copyright)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", "X"))
        self.label_title.setText(QCoreApplication.translate("MainWindow", "<strong>Frux\'s</strong> BOT"))
        self.label_error.setText(QCoreApplication.translate("MainWindow", "--<strong>ERROR!</strong>--"))
        self.label_errorInfo.setText(QCoreApplication.translate("MainWindow", "{}"))
        self.label_contact.setText(QCoreApplication.translate("MainWindow", "<strong>CONTACT </strong>  @Frux#0063"))
        self.label_copyright.setText(QCoreApplication.translate("MainWindow", "??COPYRIGHT, FRUXC"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
