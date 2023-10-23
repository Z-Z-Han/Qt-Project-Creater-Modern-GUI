# Import QtWidget and QtCore from PySide6
from PySide6 import QtWidgets, QtGui
# import QMessagebox from PySide6
from PySide6.QtWidgets import QMessageBox

import os
import sys
import json
import webbrowser

# 
from ThemePreview.main import MainWindow

# Create main class
# ########################################################################
class Functions():
    def main(self):
        #######################################################################
        # CUSTOMIZE PROGRESS BAR
        #######################################################################
        # self.ui.projectGeneratingFormProgress.updateFormProgressIndicator(
        #     # Set font color
        #     color = "#fff", 
        #     # Set fill color
        #     fillColor = "#3d436a", 
        #     # Set fill color for warnings
        #     warningFillColor = "#ff007f",
        #     # Set fill color for errors
        #     errorFillColor = "#ff0000",
        #     # Set fill color for success
        #     successFillColor = "#ff9203",
        #     # Set number of progress steps(default is 5)
        #     formProgressCount = 5,
        #     # Set progress animation duration
        #     formProgressAnimationDuration = 2000, #2seconds
        #     # Set progress animation easing curve
        #     formProgressAnimationEasingCurve = "InOutQuint",
        #     # Set progress container height
        #     height = 30,
        #     # Set progress container width
        #     width = 500,
        #     # Set default progress percentage
        #     startPercentage = 0 
        # )

        # SET PROGRESS BAR VALUE
        self.ui.creatingProgressBar.rpb_setMaximum(420) 

        # SET PROGRESS BAR STYLE
        self.ui.creatingProgressBar.rpb_setBarStyle('Donet')

        # SET PROGRESS BAR LINE COLOR
        self.ui.creatingProgressBar.rpb_setLineColor((255, 146, 3)) #ARGUMENT RGB AS A TUPLE

        #CHANGING THE PATH COLOR
        self.ui.creatingProgressBar.rpb_setPathColor((255, 255, 200))

        #SET PROGRESS BAR TEXT COLOR
        self.ui.creatingProgressBar.rpb_setTextColor((233, 30, 99)) #ARGUMENT RGB AS A TUPLE

        # SET PROGRESS BAR STARTING POSITION
        # North, East, West, South
        self.ui.creatingProgressBar.rpb_setInitialPos('West') #WEST AS STARTING POSITION.

        #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
        # Value, Percentage
        self.ui.creatingProgressBar.rpb_setTextFormat('Percentage')

        #SET PROGRESS BAR FONT
        self.ui.creatingProgressBar.rpb_setTextFont('Arial')
        
        #TEXT HIDDEN
        self.ui.creatingProgressBar.rpb_enableText(True) 

        #SET PROGRESS BAR LINE WIDTH 
        self.ui.creatingProgressBar.rpb_setLineWidth(10)

        #PATH WIDTH
        self.ui.creatingProgressBar.rpb_setPathWidth(15)

        #SET PROGRESS BAR LINE CAP
        # RoundCap, SquareCap
        self.ui.creatingProgressBar.rpb_setLineCap('RoundCap')

        #LINE STYLE
        # DotLine, DashLine
        # self.ui.creatingProgressBar.rpb_setLineStyle('DotLine')


        self.ui.to_page2.clicked.connect(lambda: 
            Functions.validateAppDetails(self)
        )
        self.ui.back_to_page1.clicked.connect(lambda: self.ui.projectGeneratingFormProgress.animateFormProgress(20))
        self.ui.to_page3.clicked.connect(lambda: self.ui.projectGeneratingFormProgress.animateFormProgress(60))
        self.ui.to_page4.clicked.connect(lambda: self.ui.projectGeneratingFormProgress.animateFormProgress(80))
        self.ui.back_to_page2.clicked.connect(lambda: self.ui.projectGeneratingFormProgress.animateFormProgress(40))
        self.ui.back_to_page3.clicked.connect(lambda: self.ui.projectGeneratingFormProgress.animateFormProgress(60))
 

        # Context menus
        self.tutorialMenu = QtWidgets.QMenu()
        self.tutorialMenu.addAction("YouTube", lambda: Functions.openYouTubeTutorials(self))
        self.tutorialMenu.addAction("GitHub", lambda: Functions.openGithubTutorials(self))

        self.ui.tutorialsBtn.setMenu(self.tutorialMenu)

        self.supportMenu = QtWidgets.QMenu()
        self.supportMenu.addAction("Patreon", lambda: Functions.openPatreon(self))
        self.supportMenu.addAction("PayPal", lambda: Functions.openPayPal(self))
        self.supportMenu.addAction("YouTube", lambda: Functions.openYouTubeTutorials(self))

        self.ui.supportHBtn.setMenu(self.supportMenu)

        self.resourcesMenu = QtWidgets.QMenu()
        self.resourcesMenu.addAction("QT Doc", lambda: Functions.openQTDoc(self))
        self.resourcesMenu.addAction("PySide2 Doc", lambda: Functions.openPySide2Doc(self))
        self.resourcesMenu.addAction("PySide6 Doc", lambda: Functions.openPySide6Doc(self))
        self.resourcesMenu.addAction("PyQt5 Doc", lambda: Functions.openPyQt5Doc(self))
        self.resourcesMenu.addAction("PyQt6 Doc", lambda: Functions.openPyQt6Doc(self))
        self.resourcesMenu.addAction("QML Doc", lambda: Functions.openQMLDoc(self))

        self.ui.resourcesBtn.setMenu(self.resourcesMenu)

        self.templatesMenu = QtWidgets.QMenu()
        self.templatesMenu.addAction("Browse Templates", lambda: Functions.openBrowseTemplates(self))
        self.templatesMenu.addAction("Upload Templates", lambda: Functions.openUploadTemplates(self))

        self.ui.templatesBtn.setMenu(self.templatesMenu)

        self.helpMenu = QtWidgets.QMenu()
        self.helpMenu.addAction("Help", lambda: Functions.openHelp(self))
        self.helpMenu.addAction("About", lambda: Functions.openAbout(self))
        self.helpMenu.addAction("Settings", lambda: Functions.openSettings(self))

        self.ui.helpBtn.setMenu(self.helpMenu)

        # Select app logo
        self.ui.selectLogoBtn.clicked.connect(lambda: Functions.selectAppLogo(self))
        # Select icons color
        self.ui.pickIconColorBtn.clicked.connect(lambda: Functions.selectIconsColor(self))
        # Select other project resources
        self.ui.otherResourcesBtn.clicked.connect(lambda: Functions.selectResources(self))
        # Select project ui template from local storage
        self.ui.uiFromLocalStorageBtn.clicked.connect(lambda: Functions.selectUiTemplateFromLocalStorage(self))

        # Add click event to the select templates button
        # the widgets are: emptyUiTemplate, moreTemplates, uiFromLocalStorageBtn
        self.clickedWidget = self.ui.emptyUiTemplate
        self.ui.emptyUiTemplate.mouseReleaseEvent = lambda event: Functions.styleClickedWidget(self, self.ui.emptyUiTemplate)
        self.ui.moreTemplates.mouseReleaseEvent = lambda event: Functions.styleClickedWidget(self, self.ui.moreTemplates)
        self.ui.uiFromLocalStorageBtn.clicked.connect(lambda: Functions.styleClickedWidget(self, self.ui.uiFromLocalStorageBtn))

        # Add click event to the select app theme color button
        self.ui.pickTextColorBtn.clicked.connect(lambda: Functions.selectTextColor(self))
        self.ui.pickBackgroundColorBtn.clicked.connect(lambda: Functions.selectBackgroundColor(self))
        self.ui.pickAppAccentColorBtn.clicked.connect(lambda: Functions.selectAppAccentColor(self))

        # Preview app theme
        self.ui.previewAppThemeBtn.clicked.connect(lambda: Functions.previewAppTheme(self))

        # Auto-fill app org and domain on appName change
        self.ui.appName.textChanged.connect(lambda: Functions.autoFillAppOrgAndDomain(self))

        # Set default variables
        self.iconsColor = None
        self.appLogo = None
        self.appTextColor = None
        self.appBackgroundColor = None
        self.appAccentColor = None
        self.appResources = None
        self.appUiTemplate = None
        self.appUiTemplatePath = None
        self.appUiTemplateType = None
        self.appUiTemplateFromLocalStorage = None
        

    # Auto-fill app org and domain on appName change
    def autoFillAppOrgAndDomain(self):
        appName = self.ui.appName.text()
        self.ui.orgName.setText(appName.capitalize()+" Organization")
        # remove spaces for domain
        appName = appName.replace(" ", "")
        self.ui.orgDormain.setText(appName.lower()+".com")


    def openYouTubeTutorials(self):
        # Open spinntv youtube channel link in the default browser
        webbrowser.open("https://www.youtube.com/channel/UCJVsWdUC3M8p-q67RXPujkg")

    def openGithubTutorials(self):
        # Open spinntv github channel link in the default browser
        webbrowser.open("https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets")

    def openPatreon(self):
        # Open spinntv patreon channel link in the default browser
        webbrowser.open("https://www.patreon.com/spinntv")

    def openPayPal(self):
        # Open spinntv paypal channel link in the default browser
        # webbrowser.open("https://www.paypal.com/paypalme/spinntv")
        pass

    def openQTDoc(self):
        # Open QT documentation link in the default browser
        webbrowser.open("https://doc.qt.io/qt-6/index.html")

    def openPySide2Doc(self):
        # Open PySide2 documentation link in the default browser
        webbrowser.open("https://pypi.org/project/PySide2/")

    def openPySide6Doc(self):
        # Open PySide6 documentation link in the default browser
        webbrowser.open("https://pypi.org/project/PySide6/")

    def openPyQt5Doc(self):
        # Open PyQt5 documentation link in the default browser
        webbrowser.open("https://pypi.org/project/PyQt5/")

    def openPyQt6Doc(self):
        # Open PyQt6 documentation link in the default browser
        webbrowser.open("https://pypi.org/project/PyQt6/")

    def openQMLDoc(self):
        # Open QML documentation link in the default browser
        webbrowser.open("https://doc.qt.io/qt-6/qtqml-index.html")

    def openBrowseTemplates(self):
        # Alert feature coming soon
        try:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)

            self.msg.setText("Feature coming soon!")
            self.msg.setInformativeText("Show more details...")
            self.msg.setWindowTitle("Feature coming soon!")
            self.msg.setDetailedText("This feature is coming soon, please check back later.")
            self.msg.setStandardButtons(QMessageBox.Ok)

            retval = self.msg.exec_()

        except Exception as e:
            raise Exception("Error: "+str(e))

    def openUploadTemplates(self):
        # Alert feature coming soon
        try:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)

            self.msg.setText("Feature coming soon!")
            self.msg.setInformativeText("Show more details...")
            self.msg.setWindowTitle("Feature coming soon!")
            self.msg.setDetailedText("This feature is coming soon, please check back later.")
            self.msg.setStandardButtons(QMessageBox.Ok)

            retval = self.msg.exec_()

        except Exception as e:
            raise Exception("Error: "+str(e))

    def openHelp(self):
        pass
    def openAbout(self):
        # Alert about the app
        try:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("About QT Project Creator App")
            self.msg.setText("This app is created by Khamisi Kibet. It is a free and open source app. You can use it to create QT projects. \nApp version: 1.0.0\nApp license: MIT\nContact: spinncompany@gmail.com")
            self.msg.setStandardButtons(QMessageBox.Ok)

            retval = self.msg.exec_()

        except Exception as e:
            raise Exception("Error: "+str(e))
    def openSettings(self):
        # go to settings page
        self.ui.mainBodyPages.setCurrentWidget(self.ui.settingsPage)

    # Validate app details
    def validateAppDetails(self):
        # check if appName is empty
        if len(self.ui.appName.text()) < 1:
            # Display the message
            self.ui.label_19.setText("Please enter an app name")
            # Set the color to red
            self.ui.label_19.setStyleSheet("color: red")
            # Return false
            return False
        
        # check if orgName is empty
        if len(self.ui.orgName.text()) < 1:
            # Display message
            self.ui.label_19.setText("Please enter an organization name")
            # Set the color to red
            self.ui.label_19.setStyleSheet("color: red")
            # Return false
            return False

        # check if orgDormain is empty
        if len(self.ui.orgDormain.text()) < 1:
            # Display message
            self.ui.label_19.setText("Please enter an organization domain")
            # Set the color to red
            self.ui.label_19.setStyleSheet("color: red")
            # Return false
            return False
            
        self.ui.projectGeneratingFormProgress.animateFormProgress(40)
        # Go to page 2
        self.ui.projectWizardPages.setCurrentIndex(1)
        # Return true
        return True

    # Select app logo
    def selectAppLogo(self):
        # Select image from file dialog
        self.appLogo = QtWidgets.QFileDialog.getOpenFileName(self, 'Select App Logo', '', 'Images (*.png *.jpg *.jpeg)')[0]
        # Set the image to the label
        self.ui.appLogoLabel.setPixmap(QtGui.QPixmap(self.appLogo))

    # Create color picker dialog using QColorDialog
    def pickColor(self):
        # Create color picker dialog
        self.pickedColor = QtWidgets.QColorDialog.getColor()
        # Return the color
        return self.pickedColor
    
    # Select icons color
    def selectIconsColor(self):
        # get color
        self.iconsColor = Functions.pickColor(self)
        # Set the color to the button
        self.ui.pickIconColorBtn.setStyleSheet("background-color: {};".format(self.iconsColor.name()))
        # Display color selected in the label
        self.ui.iconColorLabel.setText(self.iconsColor.name())

    # Select multiple files for project resources
    def selectResources(self):
        # Select all type of files
        self.resources = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select Resources', '', 'All Files (*)')[0]
        # Get total number of files
        self.totalResources = len(self.resources)
        # Display the number of files
        self.ui.resourcesCount.setText(str(self.totalResources)+" files selected")

    # Select ui template from file dialog(.ui files)
    def selectUiTemplateFromLocalStorage(self):
        # Select ui template from file dialog
        self.uiTemplate = QtWidgets.QFileDialog.getOpenFileName(self, 'Select UI Template', '', 'UI Files (*.ui)')[0]
        # Set the template to the label
        self.ui.selectedUi.setText(self.uiTemplate)

    # Style the clicked widget by adding a border
    # Border color is rgb(255, 146, 3), border width is 2px
    # then reomve the border from the previous clicked widget
    # the widgets are: emptyUiTemplate, moreTemplates, uiFromLocalStorageBtn
    def styleClickedWidget(self, widget):
        # get widget name
        widgetName = widget.objectName()
        # Apply border style using widget name
        # Set the border color
        widget.setStyleSheet("#"+widgetName+"{border: 2px solid rgb(255, 146, 3);}")
        # Remove the border from the previous clicked widget
        if self.clickedWidget != None:
            self.clickedWidget.setStyleSheet("border: none;")
        # Set the clicked widget to the current clicked widget
        self.clickedWidget = widget

        # check clicked widget name and update the ui template (selectedUi) label
        if widgetName == "emptyUiTemplate":
            self.ui.selectedUi.setText("Empty UI selected")
        elif widgetName == "moreTemplates":
            self.ui.selectedUi.setText("More Templates selected")
        elif widgetName == "uiFromLocalStorageBtn":
            # name will be set from local storage
            pass

    
    # App theme
    # Select background color using QColorDialog
    def selectBackgroundColor(self):
        # get color
        self.backgroundColor = Functions.pickColor(self)
        # Set the color to the button
        self.ui.pickBackgroundColorBtn.setStyleSheet("background-color: {};".format(self.backgroundColor.name()))
        # Display color selected in the label
        self.ui.backgroundColorLabel.setText(self.backgroundColor.name())
    # Select text color using QColorDialog
    def selectTextColor(self):
        # get color
        self.textColor = Functions.pickColor(self)
        # Set the color to the button
        self.ui.pickTextColorBtn.setStyleSheet("background-color: {};".format(self.textColor.name()))
        # Display color selected in the label
        self.ui.textColorLabel.setText(self.textColor.name())
    # Select app accent color using QColorDialog
    def selectAppAccentColor(self):
        # get color
        self.appAccentColor = Functions.pickColor(self)
        # Set the color to the button
        self.ui.pickAppAccentColorBtn.setStyleSheet("background-color: {};".format(self.appAccentColor.name()))
        # Display color selected in the label
        self.ui.appAccentColorLabel.setText(self.appAccentColor.name())

    # Preview app theme
    def previewAppTheme(self):
        # Start by updating the json file with the new values
        Functions.updateThemePreviewJsonFile(self)  
        # Open the theme preview file by running the main.py file inside theme preview folder
        # self.main = MainWindow()
        # self.main.show()

        os.system('python ThemePreview/main.py')



    # Update the theme preview json file
    def updateThemePreviewJsonFile(self):
        # Open the style.json file inside themepreview folder(ThemePreview/style.json)
        with open(os.path.join(os.path.dirname(__file__), "ThemePreview", "style.json"), "r+") as jsonFile:
            # Read the json file
            jsonData = json.load(jsonFile)
            # Update the json file with the new values
            if "QMainWindow" in jsonData:
                for QMainWindow in jsonData["QMainWindow"]:
                    # Set window tittle
                    QMainWindow["tittle"] = self.ui.appName.text()

            ########################################################################
            ## QSETTINGS
            ########################################################################
            if "QSettings" in jsonData:
                for settings in jsonData["QSettings"]:
                    if "AppSettings" in settings:
                        appSettings = settings['AppSettings']

                        appSettings["ApplicationName"] = self.ui.appName.text()
                        
                        appSettings["OrginizationName"] = self.ui.orgName.text()
                            
                        appSettings["OrginizationDormain"] = self.ui.orgDormain.text()
            
                    ########################################################################
                    ## App theme
                    ########################################################################
                    if "ThemeSettings" in settings:
                        for themeSettings in settings['ThemeSettings']:
                            if "CustomTheme" in themeSettings:
                                for customTheme in themeSettings['CustomTheme']:
                                    customTheme["Background-color"] = self.backgroundColor.name()
                                    customTheme["Text-color"] = self.textColor.name()
                                    customTheme["Accent-color"] = self.appAccentColor.name()
                                    # if iconsColor is undefined, set it to the accent color, else set it to the text color
                                    if self.iconsColor == None:
                                        try:
                                            customTheme["Icons-color"] = self.appAccentColor.name()
                                        except:
                                            customTheme["Icons-color"] = self.textColor.name()
                                    else:
                                        customTheme["Icons-color"] = self.iconsColor.name()
                                    customTheme["Create-icons"] = True
                                    customTheme["Theme-name"] = "Default-Theme"

            ########################################################################
            # Update the json file
            ########################################################################
            jsonFile.seek(0)
            jsonFile.write(json.dumps(jsonData, indent=4))
            jsonFile.truncate()
            jsonFile.close()
            ########################################################################




