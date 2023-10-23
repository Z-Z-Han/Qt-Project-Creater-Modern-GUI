########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from importlib import reload
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

########################################################################
# IMPORT Main Functions
from MainFunctions import *


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainAppWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles={
            "JsonStyles/main.json",
            "JsonStyles/default.json"
        })
        ########################################################################
   
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        # self.show() 
        #######################################################################

        QAppSettings.updateAppSettings(self)

        # Run main functions
        Functions.main(self)

        # Add themes to the combobox
        self.addTheme()

    ########################################################################
    ## Function to add themes to the combobox
    ########################################################################
    def addTheme(self):
        ########################################################################
        # READ THE CURRENT THEME NAME FROM THE SETTINGS VALUE
        # QSETTINGS CLASS CAN BE USED TO STORE DIFFERENT APP CONFIGURATIONS WHICH
        # WILL BE REMEMBERED EVEN AFTER CLOSING THE APP
        # FOR QSETTINGS TO WORK YOU HAVE TO SUBMIT YOUR ORGANIZATION NAME,
        # APP NAME AND DOMAIN NAME(CHECK THE JSON FILE)
        ########################################################################
        settings = QSettings()
        THEME = settings.value("THEME")
        # READ ALL THEME NAMES CREATED FROM THE JSON FILE
        # NOTE THAT TWO THEMES (LIGHT AND DARK) WILL BE AUTOMATICALLY ADDED TO THE LIST
        # WHEN CREATING THEMES ON YOUR JSON FILE AVOID USING LIGHT OR DARK AS YOUR THEME
        # NAME
        themeCount = -1
        for theme in self.ui.themes:
            themeCount += 1
            # Add themes to the theme list
            self.ui.appThemesList.addItem(theme.name, theme.name)
            if theme.name == THEME:
                self.ui.appThemesList.setCurrentIndex(themeCount)
        # CHANGE APP THEME WHEN THE USER SELECTS A DIFFERENT THEME FROM THE LIST
        self.ui.appThemesList.currentTextChanged.connect(lambda: self.changeAppTheme())

    ########################################################################
    ## Function to change the app theme
    ########################################################################
    def changeAppTheme(self):
        settings = QSettings()

        # self.showNotification("""When changing the app theme,
        #     new icons may be generated if the current them icons color do not match
        #     with the new theme icons color.
        #     Check the progress bar on the footer for theme generation progress.
        #     """)

        selectedTheme = self.ui.appThemesList.currentData()
        currentTheme = settings.value("THEME")
        if currentTheme != selectedTheme:
            for theme in self.ui.themes:
                if theme.name == selectedTheme:
                    # CHANGE THE THEME NAME IN SETTINGS
                    settings.setValue("THEME", theme.name);
                    # print(theme.name)

                    # RE APPLY THE NEW SETINGS
                    # CompileStyleSheet might also work
                    # CompileStyleSheet.applyCompiledSass(self)
                    QAppSettings.updateAppSettings(self)

                    # APPLY NEW THEME COLORS TO BUTTON GROUP
                    # self.ui.homeBtn.setButtonGroupActiveStyle("background-color: "+self.theme.COLOR_BACKGROUND_3)
                    # self.ui.settingsBtn.setButtonGroupActiveStyle("background-color: "+self.theme.COLOR_ACCENT_2)

                    # IF NEW ICONS WILL BE GENERATED THE APP HAS TO BE RESTARTED FOR THE NEW ICONS TO BE APPLIED
                    # 

    ########################################################################
    ## GET THE THEME CHANGE PROGRESS
    ########################################################################
    # sassCompilationProgress() is the default function that sass compiler
    # will look for and return the progress value to 
    def sassCompilationProgress(self, n):
        # n is the percentage progress value
        # print(n)
        self.ui.activityProgress.setValue(n)
        if n == 100:
            self.ui.activityProgress.setValue(0)
            # self.showNotification("Theme change complete")

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainAppWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
