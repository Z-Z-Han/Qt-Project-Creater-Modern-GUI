# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashcLIqSY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 364)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #000;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.shoe_border_frame = QFrame(self.centralwidget)
        self.shoe_border_frame.setObjectName(u"shoe_border_frame")
        self.shoe_border_frame.setGeometry(QRect(330, 79, 221, 181))
        self.shoe_border_frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.119, x2:0.539, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.455882 rgba(229, 229, 229, 255), stop:1 rgba(83, 195, 223, 255))")
        self.shoe_border_frame.setFrameShape(QFrame.StyledPanel)
        self.shoe_border_frame.setFrameShadow(QFrame.Raised)
        self.shoe_frame = QFrame(self.centralwidget)
        self.shoe_frame.setObjectName(u"shoe_frame")
        self.shoe_frame.setGeometry(QRect(300, 80, 231, 251))
        self.shoe_frame.setStyleSheet(u"image: url(:/images/images/logo.png);")
        self.shoe_frame.setFrameShape(QFrame.StyledPanel)
        self.shoe_frame.setFrameShadow(QFrame.Raised)
        self.more_info_frame = QFrame(self.centralwidget)
        self.more_info_frame.setObjectName(u"more_info_frame")
        self.more_info_frame.setGeometry(QRect(10, 210, 371, 141))
        self.more_info_frame.setStyleSheet(u"background-color: #f4f5f5;\n"
"border-radius: 20px;")
        self.more_info_frame.setFrameShape(QFrame.StyledPanel)
        self.more_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.more_info_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, -1, 40, -1)
        self.loadingstatus = QLabel(self.more_info_frame)
        self.loadingstatus.setObjectName(u"loadingstatus")
        font = QFont()
        font.setFamily(u"Noto Serif Display")
        font.setPointSize(15)
        self.loadingstatus.setFont(font)
        self.loadingstatus.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.loadingstatus.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.loadingstatus)

        self.my_progressBar = QProgressBar(self.more_info_frame)
        self.my_progressBar.setObjectName(u"my_progressBar")
        self.my_progressBar.setMinimumSize(QSize(0, 15))
        self.my_progressBar.setMaximumSize(QSize(16777215, 15))
        self.my_progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	border-style: none;\n"
"	border-radius: 7px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 82, 0, 255), stop:0.509804 rgba(254, 195, 0, 255), stop:1 rgba(255, 70, 0, 255));\n"
"	border-radius: 7px;\n"
"}")
        self.my_progressBar.setValue(24)

        self.verticalLayout.addWidget(self.my_progressBar)

        self.loading_progress_status = QLabel(self.more_info_frame)
        self.loading_progress_status.setObjectName(u"loading_progress_status")
        self.loading_progress_status.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.loading_progress_status.setAlignment(Qt.AlignCenter)
        self.loading_progress_status.setWordWrap(True)

        self.verticalLayout.addWidget(self.loading_progress_status)

        self.app_info = QLabel(self.more_info_frame)
        self.app_info.setObjectName(u"app_info")
        font1 = QFont()
        font1.setFamily(u"Noto Serif Display")
        self.app_info.setFont(font1)
        self.app_info.setStyleSheet(u"border: none;\n"
"background-color: transparent;\n"
"color: rgb(28, 20, 59);")
        self.app_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.app_info)

        MainWindow.setCentralWidget(self.centralwidget)
        self.more_info_frame.raise_()
        self.shoe_border_frame.raise_()
        self.shoe_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadingstatus.setText(QCoreApplication.translate("MainWindow", u"QT Project Creator", None))
        self.loading_progress_status.setText(QCoreApplication.translate("MainWindow", u"Please wait....", None))
        self.app_info.setText(QCoreApplication.translate("MainWindow", u"Spinn Design", None))
    # retranslateUi

