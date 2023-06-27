# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceoYSSuk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from Custom_Widgets.Widgets import QCustomStackedWidget
from Custom_Widgets.Widgets import FormProgressIndicator
from PySide2extn.RoundProgressBar import roundProgressBar
from Custom_Widgets.Widgets import QCustomSlideMenu

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 617)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.centralwidget)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout = QHBoxLayout(self.headerContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QWidget(self.headerContainer)
        self.logo.setObjectName(u"logo")
        self.verticalLayout_32 = QVBoxLayout(self.logo)
        self.verticalLayout_32.setSpacing(5)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 5)
        self.logoImg = QLabel(self.logo)
        self.logoImg.setObjectName(u"logoImg")
        self.logoImg.setMinimumSize(QSize(50, 50))
        self.logoImg.setMaximumSize(QSize(50, 50))
        self.logoImg.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.logoImg.setScaledContents(True)

        self.verticalLayout_32.addWidget(self.logoImg, 0, Qt.AlignTop)

        self.menuBtn = QPushButton(self.logo)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_32.addWidget(self.menuBtn)


        self.horizontalLayout.addWidget(self.logo, 0, Qt.AlignLeft)

        self.widget_4 = QWidget(self.headerContainer)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.widget_4)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 5)
        self.frame_12 = QFrame(self.header)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.label, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_12)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 5)
        self.helpBtn = QPushButton(self.frame)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpBtn.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon1)
        self.helpBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.helpBtn)

        self.minimizeBtn = QPushButton(self.frame)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon2)
        self.minimizeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon3)
        self.restoreBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon4)
        self.closeBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.closeBtn)


        self.horizontalLayout_3.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.homeBtn = QPushButton(self.frame_3)
        self.homeBtn.setObjectName(u"homeBtn")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.homeBtn.setFont(font1)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon5)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.homeBtn)

        self.tutorialsBtn = QPushButton(self.frame_3)
        self.tutorialsBtn.setObjectName(u"tutorialsBtn")
        self.tutorialsBtn.setFont(font1)
        self.tutorialsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/airplay.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tutorialsBtn.setIcon(icon6)
        self.tutorialsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.tutorialsBtn)

        self.templatesBtn = QPushButton(self.frame_3)
        self.templatesBtn.setObjectName(u"templatesBtn")
        self.templatesBtn.setFont(font1)
        self.templatesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.templatesBtn.setIcon(icon7)
        self.templatesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.templatesBtn)

        self.resourcesBtn = QPushButton(self.frame_3)
        self.resourcesBtn.setObjectName(u"resourcesBtn")
        self.resourcesBtn.setFont(font1)
        self.resourcesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/codepen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resourcesBtn.setIcon(icon8)
        self.resourcesBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.resourcesBtn)

        self.supportHBtn = QPushButton(self.frame_3)
        self.supportHBtn.setObjectName(u"supportHBtn")
        self.supportHBtn.setFont(font1)
        self.supportHBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/dollar-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.supportHBtn.setIcon(icon9)
        self.supportHBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.supportHBtn)


        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.generateProjectBtn = QPushButton(self.frame_4)
        self.generateProjectBtn.setObjectName(u"generateProjectBtn")
        self.generateProjectBtn.setFont(font1)
        self.generateProjectBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/tool.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generateProjectBtn.setIcon(icon10)
        self.generateProjectBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.generateProjectBtn)

        self.loginBtn = QPushButton(self.frame_4)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setFont(font1)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/log-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon11)
        self.loginBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.loginBtn)


        self.horizontalLayout_4.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContainer)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sideMenu = QCustomSlideMenu(self.mainBodyContainer)
        self.sideMenu.setObjectName(u"sideMenu")
        self.sideMenu.setMinimumSize(QSize(0, 470))
        self.sideMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_33 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_15 = QWidget(self.sideMenu)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(134, 458))
        self.verticalLayout_34 = QVBoxLayout(self.widget_15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_34.addWidget(self.label_2)


        self.verticalLayout_33.addWidget(self.widget_15)


        self.horizontalLayout_8.addWidget(self.sideMenu)

        self.mainBodyPages = QCustomStackedWidget(self.mainBodyContainer)
        self.mainBodyPages.setObjectName(u"mainBodyPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_3 = QVBoxLayout(self.homePage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.homePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(796, 359))
        self.scrollArea.setMaximumSize(QSize(796, 359))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 792, 355))
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 20, 411, 301))
        self.widget.setMinimumSize(QSize(411, 301))
        self.widget.setMaximumSize(QSize(411, 301))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, -1, 50, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.supportBtn = QPushButton(self.frame_5)
        self.supportBtn.setObjectName(u"supportBtn")
        self.supportBtn.setIcon(icon9)
        self.supportBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.supportBtn, 0, Qt.AlignLeft)

        self.getStartedBtn = QPushButton(self.frame_5)
        self.getStartedBtn.setObjectName(u"getStartedBtn")
        self.getStartedBtn.setIcon(icon10)
        self.getStartedBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.getStartedBtn, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 350, 350))
        self.label_3.setMinimumSize(QSize(350, 350))
        self.label_3.setMaximumSize(QSize(350, 350))
        self.label_3.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label_3.setScaledContents(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3.raise_()
        self.widget.raise_()

        self.verticalLayout_3.addWidget(self.scrollArea, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.mainBodyPages.addWidget(self.homePage)
        self.projectPage = QWidget()
        self.projectPage.setObjectName(u"projectPage")
        self.verticalLayout_8 = QVBoxLayout(self.projectPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_6 = QWidget(self.projectPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.projectGeneratingFormProgress = FormProgressIndicator(self.widget_6)
        self.projectGeneratingFormProgress.setObjectName(u"projectGeneratingFormProgress")

        self.verticalLayout_14.addWidget(self.projectGeneratingFormProgress, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_8.addWidget(self.widget_6, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.projectPage)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy2)
        self.widget_7.setMinimumSize(QSize(700, 0))
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_16 = QLabel(self.widget_7)
        self.label_16.setObjectName(u"label_16")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_16)

        self.projectWizardPages = QCustomStackedWidget(self.widget_7)
        self.projectWizardPages.setObjectName(u"projectWizardPages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_18 = QVBoxLayout(self.page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_8 = QWidget(self.page)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.widget_8.setMinimumSize(QSize(250, 0))
        self.verticalLayout_16 = QVBoxLayout(self.widget_8)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 5, 0, 5)
        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_18.setFont(font4)

        self.verticalLayout_16.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.widget_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.appName = QLineEdit(self.frame_10)
        self.appName.setObjectName(u"appName")
        self.appName.setFont(font1)

        self.verticalLayout_17.addWidget(self.appName)

        self.orgName = QLineEdit(self.frame_10)
        self.orgName.setObjectName(u"orgName")
        self.orgName.setFont(font1)
        self.orgName.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_17.addWidget(self.orgName)

        self.orgDormain = QLineEdit(self.frame_10)
        self.orgDormain.setObjectName(u"orgDormain")
        self.orgDormain.setFont(font1)
        self.orgDormain.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_17.addWidget(self.orgDormain)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.to_page2 = QPushButton(self.widget_8)
        self.to_page2.setObjectName(u"to_page2")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setBold(True)
        font5.setWeight(75)
        self.to_page2.setFont(font5)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/fast-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.to_page2.setIcon(icon12)
        self.to_page2.setIconSize(QSize(20, 20))

        self.verticalLayout_16.addWidget(self.to_page2, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.widget_8, 0, Qt.AlignHCenter)

        self.projectWizardPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_21 = QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_9 = QWidget(self.page_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.widget_9.setMinimumSize(QSize(250, 0))
        self.gridLayout = QGridLayout(self.widget_9)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 5, 0, 5)
        self.back_to_page1 = QPushButton(self.widget_9)
        self.back_to_page1.setObjectName(u"back_to_page1")
        self.back_to_page1.setFont(font5)
        self.back_to_page1.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/rewind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_page1.setIcon(icon13)
        self.back_to_page1.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.back_to_page1, 10, 1, 1, 1, Qt.AlignLeft)

        self.label_23 = QLabel(self.widget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)
        self.label_23.setWordWrap(True)

        self.gridLayout.addWidget(self.label_23, 7, 2, 1, 1)

        self.otherResourcesBtn = QPushButton(self.widget_9)
        self.otherResourcesBtn.setObjectName(u"otherResourcesBtn")
        self.otherResourcesBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/folder-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.otherResourcesBtn.setIcon(icon14)
        self.otherResourcesBtn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.otherResourcesBtn, 7, 1, 1, 1)

        self.selectLogoBtn = QPushButton(self.widget_9)
        self.selectLogoBtn.setObjectName(u"selectLogoBtn")
        self.selectLogoBtn.setFont(font1)
        self.selectLogoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectLogoBtn.setIcon(icon15)
        self.selectLogoBtn.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.selectLogoBtn, 3, 1, 1, 1, Qt.AlignHCenter)

        self.pickIconColorBtn = QPushButton(self.widget_9)
        self.pickIconColorBtn.setObjectName(u"pickIconColorBtn")
        self.pickIconColorBtn.setMinimumSize(QSize(40, 40))
        self.pickIconColorBtn.setMaximumSize(QSize(40, 40))
        self.pickIconColorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/mouse-pointer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pickIconColorBtn.setIcon(icon16)
        self.pickIconColorBtn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pickIconColorBtn, 5, 1, 1, 1, Qt.AlignHCenter)

        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setWordWrap(True)

        self.gridLayout.addWidget(self.label_22, 5, 2, 1, 1)

        self.iconColorLabel = QLabel(self.widget_9)
        self.iconColorLabel.setObjectName(u"iconColorLabel")

        self.gridLayout.addWidget(self.iconColorLabel, 5, 3, 1, 1)

        self.resourcesCount = QLabel(self.widget_9)
        self.resourcesCount.setObjectName(u"resourcesCount")

        self.gridLayout.addWidget(self.resourcesCount, 7, 3, 1, 1)

        self.to_page3 = QPushButton(self.widget_9)
        self.to_page3.setObjectName(u"to_page3")
        self.to_page3.setFont(font5)
        self.to_page3.setCursor(QCursor(Qt.PointingHandCursor))
        self.to_page3.setIcon(icon12)
        self.to_page3.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.to_page3, 10, 3, 1, 1, Qt.AlignRight)

        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 5)

        self.label_20 = QLabel(self.widget_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 4)

        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 2, 1, 1)

        self.appLogoLabel = QLabel(self.widget_9)
        self.appLogoLabel.setObjectName(u"appLogoLabel")
        self.appLogoLabel.setMinimumSize(QSize(50, 50))
        self.appLogoLabel.setMaximumSize(QSize(50, 50))
        self.appLogoLabel.setPixmap(QPixmap(u":/icons/Icons/image.png"))
        self.appLogoLabel.setScaledContents(True)

        self.gridLayout.addWidget(self.appLogoLabel, 3, 3, 1, 1)


        self.verticalLayout_21.addWidget(self.widget_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.projectWizardPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_19 = QVBoxLayout(self.page_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy2.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy2)
        self.widget_10.setMinimumSize(QSize(250, 0))
        self.gridLayout_2 = QGridLayout(self.widget_10)
        self.gridLayout_2.setSpacing(15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 5, 0, 5)
        self.label_24 = QLabel(self.widget_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 2)

        self.uiFromLocalStorageBtn = QPushButton(self.widget_10)
        self.uiFromLocalStorageBtn.setObjectName(u"uiFromLocalStorageBtn")
        self.uiFromLocalStorageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.uiFromLocalStorageBtn.setIcon(icon14)
        self.uiFromLocalStorageBtn.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.uiFromLocalStorageBtn, 6, 0, 1, 1)

        self.label_27 = QLabel(self.widget_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_27, 1, 0, 1, 2)

        self.to_page6 = QPushButton(self.widget_10)
        self.to_page6.setObjectName(u"to_page6")
        self.to_page6.setFont(font5)
        self.to_page6.setCursor(QCursor(Qt.PointingHandCursor))
        self.to_page6.setIcon(icon12)
        self.to_page6.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.to_page6, 9, 1, 1, 1, Qt.AlignRight)

        self.back_to_page2 = QPushButton(self.widget_10)
        self.back_to_page2.setObjectName(u"back_to_page2")
        self.back_to_page2.setFont(font5)
        self.back_to_page2.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_page2.setIcon(icon13)
        self.back_to_page2.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.back_to_page2, 9, 0, 1, 1, Qt.AlignLeft)

        self.moreTemplates = QFrame(self.widget_10)
        self.moreTemplates.setObjectName(u"moreTemplates")
        self.moreTemplates.setCursor(QCursor(Qt.PointingHandCursor))
        self.moreTemplates.setFrameShape(QFrame.StyledPanel)
        self.moreTemplates.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.moreTemplates)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_29 = QLabel(self.moreTemplates)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 50))
        self.label_29.setMaximumSize(QSize(50, 50))
        self.label_29.setPixmap(QPixmap(u":/icons/Icons/globe.png"))
        self.label_29.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.label_26 = QLabel(self.moreTemplates)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)
        self.label_26.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_26, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.moreTemplates, 2, 1, 4, 1)

        self.emptyUiTemplate = QFrame(self.widget_10)
        self.emptyUiTemplate.setObjectName(u"emptyUiTemplate")
        self.emptyUiTemplate.setCursor(QCursor(Qt.PointingHandCursor))
        self.emptyUiTemplate.setFrameShape(QFrame.StyledPanel)
        self.emptyUiTemplate.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.emptyUiTemplate)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_28 = QLabel(self.emptyUiTemplate)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 50))
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setPixmap(QPixmap(u":/icons/Icons/image.png"))
        self.label_28.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.label_28, 0, Qt.AlignHCenter)

        self.label_25 = QLabel(self.emptyUiTemplate)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)
        self.label_25.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_25, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.emptyUiTemplate, 2, 0, 4, 1)

        self.selectedUi = QLabel(self.widget_10)
        self.selectedUi.setObjectName(u"selectedUi")
        self.selectedUi.setWordWrap(True)

        self.gridLayout_2.addWidget(self.selectedUi, 6, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.widget_10, 0, Qt.AlignHCenter)

        self.projectWizardPages.addWidget(self.page_3)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_24 = QVBoxLayout(self.page_6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_13 = QWidget(self.page_6)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.widget_13.setMinimumSize(QSize(250, 0))
        self.gridLayout_3 = QGridLayout(self.widget_13)
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 5, 0, 5)
        self.pickBackgroundColorBtn = QPushButton(self.widget_13)
        self.pickBackgroundColorBtn.setObjectName(u"pickBackgroundColorBtn")
        self.pickBackgroundColorBtn.setFont(font1)
        self.pickBackgroundColorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/layers.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pickBackgroundColorBtn.setIcon(icon17)
        self.pickBackgroundColorBtn.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.pickBackgroundColorBtn, 3, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.back_to_page3 = QPushButton(self.widget_13)
        self.back_to_page3.setObjectName(u"back_to_page3")
        self.back_to_page3.setFont(font5)
        self.back_to_page3.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_to_page3.setIcon(icon13)
        self.back_to_page3.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.back_to_page3, 10, 1, 1, 1, Qt.AlignLeft)

        self.label_33 = QLabel(self.widget_13)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font1)
        self.label_33.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_33, 5, 2, 1, 1)

        self.pickTextColorBtn = QPushButton(self.widget_13)
        self.pickTextColorBtn.setObjectName(u"pickTextColorBtn")
        self.pickTextColorBtn.setMinimumSize(QSize(40, 40))
        self.pickTextColorBtn.setMaximumSize(QSize(40, 40))
        self.pickTextColorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pickTextColorBtn.setIcon(icon18)
        self.pickTextColorBtn.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.pickTextColorBtn, 5, 1, 1, 1, Qt.AlignHCenter)

        self.appAccentColorLabel = QLabel(self.widget_13)
        self.appAccentColorLabel.setObjectName(u"appAccentColorLabel")

        self.gridLayout_3.addWidget(self.appAccentColorLabel, 7, 3, 1, 1)

        self.pickAppAccentColorBtn = QPushButton(self.widget_13)
        self.pickAppAccentColorBtn.setObjectName(u"pickAppAccentColorBtn")
        self.pickAppAccentColorBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/layout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pickAppAccentColorBtn.setIcon(icon19)
        self.pickAppAccentColorBtn.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.pickAppAccentColorBtn, 7, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.to_page4 = QPushButton(self.widget_13)
        self.to_page4.setObjectName(u"to_page4")
        self.to_page4.setFont(font5)
        self.to_page4.setCursor(QCursor(Qt.PointingHandCursor))
        self.to_page4.setIcon(icon12)
        self.to_page4.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.to_page4, 10, 3, 1, 1, Qt.AlignRight)

        self.label_36 = QLabel(self.widget_13)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_36, 3, 2, 1, 1)

        self.backgroundColorLabel = QLabel(self.widget_13)
        self.backgroundColorLabel.setObjectName(u"backgroundColorLabel")

        self.gridLayout_3.addWidget(self.backgroundColorLabel, 3, 3, 1, 1)

        self.label_34 = QLabel(self.widget_13)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_34, 1, 0, 1, 6)

        self.label_30 = QLabel(self.widget_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)
        self.label_30.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_30, 7, 2, 1, 1)

        self.label_35 = QLabel(self.widget_13)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font4)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_35, 0, 0, 1, 4)

        self.textColorLabel = QLabel(self.widget_13)
        self.textColorLabel.setObjectName(u"textColorLabel")

        self.gridLayout_3.addWidget(self.textColorLabel, 5, 3, 1, 1)

        self.previewAppThemeBtn = QPushButton(self.widget_13)
        self.previewAppThemeBtn.setObjectName(u"previewAppThemeBtn")
        self.previewAppThemeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/icons/Icons/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previewAppThemeBtn.setIcon(icon20)
        self.previewAppThemeBtn.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.previewAppThemeBtn, 8, 3, 1, 1)


        self.verticalLayout_24.addWidget(self.widget_13, 0, Qt.AlignHCenter)

        self.projectWizardPages.addWidget(self.page_6)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_25 = QVBoxLayout(self.page_4)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_11 = QWidget(self.page_4)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy2.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy2)
        self.widget_11.setMinimumSize(QSize(250, 247))
        self.verticalLayout_23 = QVBoxLayout(self.widget_11)
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 5, 0, 5)
        self.label_31 = QLabel(self.widget_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font4)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_32)

        self.creatingProgressBar = roundProgressBar(self.widget_11)
        self.creatingProgressBar.setObjectName(u"creatingProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.creatingProgressBar.sizePolicy().hasHeightForWidth())
        self.creatingProgressBar.setSizePolicy(sizePolicy3)
        self.creatingProgressBar.setMinimumSize(QSize(150, 150))
        self.creatingProgressBar.setMaximumSize(QSize(150, 150))

        self.verticalLayout_23.addWidget(self.creatingProgressBar, 0, Qt.AlignHCenter)

        self.back_to_page6 = QPushButton(self.widget_11)
        self.back_to_page6.setObjectName(u"back_to_page6")
        self.back_to_page6.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/icons/Icons/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_to_page6.setIcon(icon21)
        self.back_to_page6.setIconSize(QSize(20, 20))

        self.verticalLayout_23.addWidget(self.back_to_page6)


        self.verticalLayout_25.addWidget(self.widget_11, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.projectWizardPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_28 = QVBoxLayout(self.page_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_12 = QWidget(self.page_5)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy2.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy2)
        self.widget_12.setMinimumSize(QSize(250, 0))
        self.gridLayout_4 = QGridLayout(self.widget_12)
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 5, 0, 5)
        self.frame_18 = QFrame(self.widget_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_18)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_39 = QLabel(self.frame_18)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 50))
        self.label_39.setMaximumSize(QSize(50, 50))
        self.label_39.setPixmap(QPixmap(u":/icons/Icons/terminal.png"))
        self.label_39.setScaledContents(True)

        self.verticalLayout_30.addWidget(self.label_39, 0, Qt.AlignHCenter)

        self.pushButton_8 = QPushButton(self.frame_18)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_30.addWidget(self.pushButton_8)


        self.gridLayout_4.addWidget(self.frame_18, 2, 0, 1, 1)

        self.frame_16 = QFrame(self.widget_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_40 = QLabel(self.frame_16)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 50))
        self.label_40.setMaximumSize(QSize(50, 50))
        self.label_40.setPixmap(QPixmap(u":/icons/Icons/folder.png"))
        self.label_40.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_40, 0, Qt.AlignHCenter)

        self.pushButton_9 = QPushButton(self.frame_16)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_27.addWidget(self.pushButton_9)


        self.gridLayout_4.addWidget(self.frame_16, 2, 1, 1, 1)

        self.frame_17 = QFrame(self.widget_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_17)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_42 = QLabel(self.frame_17)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(50, 50))
        self.label_42.setMaximumSize(QSize(50, 50))
        self.label_42.setPixmap(QPixmap(u":/icons/Icons/edit-3.png"))
        self.label_42.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.label_42, 0, Qt.AlignHCenter)

        self.pushButton_11 = QPushButton(self.frame_17)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_29.addWidget(self.pushButton_11)


        self.gridLayout_4.addWidget(self.frame_17, 2, 2, 1, 1)

        self.frame_15 = QFrame(self.widget_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_15)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_41 = QLabel(self.frame_15)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(50, 50))
        self.label_41.setMaximumSize(QSize(50, 50))
        self.label_41.setPixmap(QPixmap(u":/icons/Icons/codesandbox.png"))
        self.label_41.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.label_41, 0, Qt.AlignHCenter)

        self.pushButton_10 = QPushButton(self.frame_15)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_26.addWidget(self.pushButton_10)


        self.gridLayout_4.addWidget(self.frame_15, 2, 3, 1, 1)

        self.label_37 = QLabel(self.widget_12)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_37, 0, 0, 1, 4)

        self.label_38 = QLabel(self.widget_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_38, 1, 0, 1, 4)


        self.verticalLayout_28.addWidget(self.widget_12)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_6)

        self.projectWizardPages.addWidget(self.page_5)

        self.verticalLayout_15.addWidget(self.projectWizardPages)


        self.verticalLayout_8.addWidget(self.widget_7, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.mainBodyPages.addWidget(self.projectPage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.verticalLayout_6 = QVBoxLayout(self.loginPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.loginPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 551, 410))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 10, 0)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(350, 350))
        self.label_10.setMaximumSize(QSize(350, 350))
        self.label_10.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.userAccountPages = QCustomStackedWidget(self.widget_3)
        self.userAccountPages.setObjectName(u"userAccountPages")
        self.userAccountPages.setMinimumSize(QSize(0, 0))
        self.userAccountPages.setMaximumSize(QSize(16777215, 16777215))
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.verticalLayout_5 = QVBoxLayout(self.registerPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.registerPage)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 5, 0, 5)
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 50))
        self.label_7.setMaximumSize(QSize(50, 50))
        self.label_7.setPixmap(QPixmap(u":/icons/Icons/user-plus.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.widget_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font1)

        self.verticalLayout_11.addWidget(self.checkBox)

        self.submitRegistrationBtn = QPushButton(self.widget_2)
        self.submitRegistrationBtn.setObjectName(u"submitRegistrationBtn")
        self.submitRegistrationBtn.setFont(font5)
        self.submitRegistrationBtn.setIcon(icon11)
        self.submitRegistrationBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.submitRegistrationBtn)

        self.to_login = QPushButton(self.widget_2)
        self.to_login.setObjectName(u"to_login")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setUnderline(True)
        self.to_login.setFont(font6)

        self.verticalLayout_11.addWidget(self.to_login, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.userAccountPages.addWidget(self.registerPage)
        self.loginPage_2 = QWidget()
        self.loginPage_2.setObjectName(u"loginPage_2")
        self.verticalLayout_10 = QVBoxLayout(self.loginPage_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.loginPage_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_13 = QVBoxLayout(self.widget_5)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 5, 0, 5)
        self.label_13 = QLabel(self.widget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 50))
        self.label_13.setMaximumSize(QSize(50, 50))
        self.label_13.setPixmap(QPixmap(u":/icons/Icons/user-check.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.frame_9 = QFrame(self.widget_5)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font1)

        self.verticalLayout_9.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font1)
        self.lineEdit_7.setEchoMode(QLineEdit.Password)

        self.verticalLayout_9.addWidget(self.lineEdit_7)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.submitLoginBtn = QPushButton(self.widget_5)
        self.submitLoginBtn.setObjectName(u"submitLoginBtn")
        self.submitLoginBtn.setFont(font5)
        self.submitLoginBtn.setIcon(icon11)
        self.submitLoginBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_13.addWidget(self.submitLoginBtn)

        self.to_register = QPushButton(self.widget_5)
        self.to_register.setObjectName(u"to_register")
        self.to_register.setFont(font6)

        self.verticalLayout_13.addWidget(self.to_register, 0, Qt.AlignHCenter)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.widget_5, 0, Qt.AlignLeft)

        self.userAccountPages.addWidget(self.loginPage_2)

        self.horizontalLayout_12.addWidget(self.userAccountPages)


        self.verticalLayout_12.addWidget(self.widget_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.mainBodyPages.addWidget(self.loginPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_31 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_43 = QLabel(self.settingsPage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_43, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.settingsPage)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_44 = QLabel(self.frame_11)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_11.addWidget(self.label_44, 0, Qt.AlignRight)

        self.appThemesList = QComboBox(self.frame_11)
        self.appThemesList.setObjectName(u"appThemesList")

        self.horizontalLayout_11.addWidget(self.appThemesList, 0, Qt.AlignLeft)


        self.verticalLayout_31.addWidget(self.frame_11)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_8)

        self.mainBodyPages.addWidget(self.settingsPage)

        self.horizontalLayout_8.addWidget(self.mainBodyPages, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.mainBodyContainer)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_10 = QHBoxLayout(self.footer)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_7 = QFrame(self.footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.activityProgress = QProgressBar(self.frame_6)
        self.activityProgress.setObjectName(u"activityProgress")
        self.activityProgress.setMaximumSize(QSize(16777215, 8))
        self.activityProgress.setValue(0)
        self.activityProgress.setTextVisible(False)

        self.horizontalLayout_13.addWidget(self.activityProgress)


        self.horizontalLayout_10.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.sizeGrip = QFrame(self.footer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(10, 10))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.sizeGrip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainBodyPages.setCurrentIndex(0)
        self.projectWizardPages.setCurrentIndex(0)
        self.userAccountPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoImg.setText("")
        self.menuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT Project Creator", None))
        self.helpBtn.setText("")
        self.minimizeBtn.setText("")
        self.restoreBtn.setText("")
        self.closeBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.tutorialsBtn.setText(QCoreApplication.translate("MainWindow", u"Tutorials", None))
        self.templatesBtn.setText(QCoreApplication.translate("MainWindow", u"UI Templates", None))
        self.resourcesBtn.setText(QCoreApplication.translate("MainWindow", u"More Resources", None))
        self.supportHBtn.setText(QCoreApplication.translate("MainWindow", u"Support", None))
#if QT_CONFIG(tooltip)
        self.generateProjectBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Create a new project", None))
#endif // QT_CONFIG(tooltip)
        self.generateProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Project", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Side Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"A great way to create your QT project.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"QT Project Creator", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Launch your project with<span style=\" font-weight:600;\"> Modern U</span>I templates intergrated to work with the<span style=\" font-weight:600;\"> Custom Widgets</span>.</p><p><span style=\" font-weight:600;\">More templates</span> coming soon...</p></body></html>", None))
        self.supportBtn.setText(QCoreApplication.translate("MainWindow", u"Support Project", None))
        self.getStartedBtn.setText(QCoreApplication.translate("MainWindow", u"Get Started", None))
        self.label_3.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Generate Your QT Project", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"App Details", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Enter your app details below", None))
        self.appName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"App Name", None))
        self.orgName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Organisation Name", None))
        self.orgDormain.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Organisation Dormain", None))
        self.to_page2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.back_to_page1.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Select a folder containing more resource files(Optional)", None))
        self.otherResourcesBtn.setText("")
        self.selectLogoBtn.setText("")
        self.pickIconColorBtn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Pick icons color for auto-generated icons(Optional)", None))
        self.iconColorLabel.setText(QCoreApplication.translate("MainWindow", u"Color: #000", None))
        self.resourcesCount.setText(QCoreApplication.translate("MainWindow", u"0 Files selected", None))
        self.to_page3.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Select your app resources", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"App Resources", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Select App Logo(Optional)", None))
        self.appLogoLabel.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"UI File", None))
        self.uiFromLocalStorageBtn.setText(QCoreApplication.translate("MainWindow", u"Select from local storage", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Select the UI template", None))
        self.to_page6.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.back_to_page2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_29.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Browse More Templates", None))
        self.label_28.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Empty UI tempalate", None))
        self.selectedUi.setText(QCoreApplication.translate("MainWindow", u"Empty UI selected", None))
        self.pickBackgroundColorBtn.setText("")
        self.back_to_page3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Text Color", None))
        self.pickTextColorBtn.setText("")
        self.appAccentColorLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.pickAppAccentColorBtn.setText("")
        self.to_page4.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Main Background Color", None))
        self.backgroundColorLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Select Colors For Your App Theme(Optional)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Accent Color", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"App Theme", None))
        self.textColorLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.previewAppThemeBtn.setText(QCoreApplication.translate("MainWindow", u"Preview Theme", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Creating Your Project", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Please wait...", None))
        self.back_to_page6.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_39.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Run Your Project", None))
        self.label_40.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Open Project Folder", None))
        self.label_42.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Open Project in VS Code", None))
        self.label_41.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Open UI File in QT Designer", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"All Done!", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Select your next step.", None))
        self.label_10.setText("")
        self.label_7.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enter your information below", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Agree with our terms", None))
        self.submitRegistrationBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Already registered? Login", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Spinn Tv Inc.", None))
        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Enter your information below", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.submitLoginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.to_register.setText(QCoreApplication.translate("MainWindow", u"Not registered? Register", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Spinn Tv Inc.", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Select Theme:", None))
    # retranslateUi

