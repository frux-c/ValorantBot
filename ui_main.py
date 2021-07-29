# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzhbIGI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(610, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.closeButton = QPushButton(self.frame_3)
        self.closeButton.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setFamily("Small Fonts")
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(Qt.RightToLeft)
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
        self.verticalLayout_2.addWidget(self.frame_3)
        self.label_title = QLabel(self.frame)
        self.label_title.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.label_2 = QLabel(self.frame)
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : rgb(98, 114, 164);")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setMinimumSize(QSize(0, 90))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.farmButton = QPushButton(self.frame_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.farmButton.sizePolicy().hasHeightForWidth())
        self.farmButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.farmButton.setFont(font)
        self.farmButton.setStyleSheet(".QPushButton {\n"
"    \n"
"    border-radius:15px;\n"
"    background-color: rgb(254, 121, 199);\n"
"    color:#ffffff;\n"
"    padding:16px 31px;\n"
"    text-decoration:none;\n"
"    color: rgb(98, 114, 164);\n"
"    border:2px solid rgb(98, 114, 164);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.426, x2:1, y2:0.46, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(85, 0, 127, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(200, 144, 200);\n"
"}\n"
"")
        self.farmButton.setObjectName("farmButton")
        self.horizontalLayout.addWidget(self.farmButton)
        self.label_split = QLabel(self.frame_2)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_split.setFont(font)
        self.label_split.setLayoutDirection(Qt.LeftToRight)
        self.label_split.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_split.setAlignment(Qt.AlignCenter)
        self.label_split.setObjectName("label_split")
        self.horizontalLayout.addWidget(self.label_split)
        self.afkButton = QPushButton(self.frame_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afkButton.sizePolicy().hasHeightForWidth())
        self.afkButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        self.afkButton.setFont(font)
        self.afkButton.setStyleSheet(".QPushButton {\n"
"    \n"
"    border-radius:15px;\n"
"    background-color: rgb(254, 121, 199);\n"
"    color:#ffffff;\n"
"    padding:16px 31px;\n"
"    text-decoration:none;\n"
"    color: rgb(98, 114, 164);\n"
"    border:2px solid rgb(98, 114, 164);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.426, x2:1, y2:0.46, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(85, 0, 127, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(200, 144, 200);\n"
"}\n"
"")
        self.afkButton.setObjectName("afkButton")
        self.horizontalLayout.addWidget(self.afkButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.resolution_label = QLabel(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution_label.sizePolicy().hasHeightForWidth())
        self.resolution_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resolution_label.setFont(font)
        self.resolution_label.setAlignment(Qt.AlignCenter)
        self.resolution_label.setObjectName("resolution_label")
        self.verticalLayout_2.addWidget(self.resolution_label)
        self.label_rec_res = QLabel(self.frame)
        self.label_rec_res.setMinimumSize(QSize(0, 9))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_rec_res.setFont(font)
        self.label_rec_res.setAlignment(Qt.AlignCenter)
        self.label_rec_res.setObjectName("label_rec_res")
        self.label_rec_res.setStyleSheet("color : rgb(98, 114, 164);")
        self.verticalLayout_2.addWidget(self.label_rec_res)
        self.radio_frame = QFrame(self.frame)
        self.radio_frame.setLayoutDirection(Qt.LeftToRight)
        self.radio_frame.setFrameShape(QFrame.StyledPanel)
        self.radio_frame.setFrameShadow(QFrame.Raised)
        self.radio_frame.setObjectName("radio_frame")
        self.horizontalLayout_3 = QHBoxLayout(self.radio_frame)
        self.horizontalLayout_3.setContentsMargins(100, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radio_1080p = QRadioButton(self.radio_frame)
        self.radio_1080p.setStyleSheet("color : rgb(98, 114, 164);")
        self.radio_1080p.setChecked(True)
        self.radio_1080p.setObjectName("radio_1080p")
        self.horizontalLayout_3.addWidget(self.radio_1080p)
        self.radio_1440p = QRadioButton(self.radio_frame)
        self.radio_1440p.setStyleSheet("color : rgb(98, 114, 164);")
        self.radio_1440p.setObjectName("radio_1440p")
        self.horizontalLayout_3.addWidget(self.radio_1440p)
        self.radio_4k = QRadioButton(self.radio_frame)
        self.radio_4k.setLayoutDirection(Qt.LeftToRight)
        self.radio_4k.setStyleSheet("color : rgb(98, 114, 164);")
        self.radio_4k.setObjectName("radio_4k")
        self.horizontalLayout_3.addWidget(self.radio_4k)
        self.verticalLayout_2.addWidget(self.radio_frame)
        self.Start = QPushButton(self.frame)
        self.Start.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        self.Start.setFont(font)
        self.Start.setStyleSheet(".QPushButton {\n"
"    \n"
"    border-radius:15px;\n"
"    background-color: rgb(254, 121, 199);\n"
"    color:#ffffff;\n"
"    padding:16px 31px;\n"
"    text-decoration:none;\n"
"    color: rgb(98, 114, 164);\n"
"    border:2px solid rgb(98, 114, 164);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.426, x2:1, y2:0.46, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(85, 0, 127, 255));\n"
"    color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(200, 144, 200);\n"
"}\n"
"")
        self.Start.setObjectName("Start")
        self.verticalLayout_2.addWidget(self.Start)
        self.label = QLabel(self.frame)
        self.label.setMaximumSize(QSize(16777215, 15))
        font = QFont()
        font.setFamily("Segoe UI")
        self.label.setFont(font)
        self.label.setStyleSheet("    color: rgb(98, 114, 164);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.frame_3.raise_()
        self.label_title.raise_()
        self.label_2.raise_()
        self.frame_2.raise_()
        self.Start.raise_()
        self.label.raise_()
        self.radio_frame.raise_()
        self.label_rec_res.raise_()
        self.resolution_label.raise_()
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", "X"))
        self.label_title.setText(QCoreApplication.translate("MainWindow", "<strong>Frux\'s</strong> BOT"))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "choose between"))
        self.farmButton.setText(QCoreApplication.translate("MainWindow", "XP Farm"))
        self.label_split.setText(QCoreApplication.translate("MainWindow", "-<strong>OR</strong>-"))
        self.resolution_label.setText(QCoreApplication.translate("MainWindow", "Screen Resolution"))
        self.radio_1080p.setText(QCoreApplication.translate("MainWindow", "1920x1080"))
        self.radio_1440p.setText(QCoreApplication.translate("MainWindow", "2560x1440"))
        self.radio_4k.setText(QCoreApplication.translate("MainWindow", "3840x2160"))
        self.afkButton.setText(QCoreApplication.translate("MainWindow", "Rage AFK"))
        self.Start.setText(QCoreApplication.translate("MainWindow", "Start Bot"))
        self.label.setText(QCoreApplication.translate("MainWindow", "©COPYRIGHT, FRUXC"))

    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
