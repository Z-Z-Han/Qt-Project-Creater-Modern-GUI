# APP SPLASH SCREEN

# APP Imports
import sys
import os
from PySide6 import QtCore

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

# Import user interface file
# Splash interface
from ui_splash import *
from main import MainAppWindow

# Global values
progressBarValue = 0

# Main class/ Splash window
class SplashWindow(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)

                ########################################################################
                # APPLY JSON STYLESHEET
                ########################################################################
                # self = QMainWindow class
                # self.ui = Ui_MainWindow / user interface class
                loadJsonStyle(self, self.ui, jsonFiles={
                        "JsonStyles/splash.json",
                        "JsonStyles/default.json"
                })
                ########################################################################

                # QAppSettings.updateAppSettings(self)

                # # CHANGE THE THEME NAME IN SETTINGS
                # # Use one of the app themes from your JSON file
                # settings = QSettings()
                # settings.setValue("THEME", "Light-Orange")
                        
                # # RE APPLY THE NEW SETINGS
                # # CompileStyleSheet might also work
                # # CompileStyleSheet.applyCompiledSass(self)
                # QAppSettings.updateAppSettings(self)


                #Lets use QTIMER to delay the progressBar
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.appProgress)

                #Time interval in Milliseconds for the progressbar to change value
                self.timer.start(100)

                # Show window
                self.show()


        # Lets define appProgress function
        #Update the progressBar value
        def appProgress(self):
                # Acess the global variable progressBarValue
                global progressBarValue

                #Apply progressBarValue to the progressBar
                self.ui.my_progressBar.setValue(progressBarValue)

                #View progressBarValue and update status text or close splash screen and open main window(We'll do this on next tutorial)
                if progressBarValue > 100: 
                        # close window
                        self.close()
                        # stop timer
                        self.timer.stop()
                        # open main window
                        self.showMainWindow()

                # Lets update the loading status text as the progress changes
                elif progressBarValue < 10:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Connecting to Nike server"))

                elif progressBarValue < 20:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Logging in..."))

                elif progressBarValue < 35:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Logging in succesfully. Requesting profile..."))

                elif progressBarValue < 55:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Profile set to Spinn Design. Requesting Spinn Design profile information..."))

                elif progressBarValue < 65:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Finalizing profile setup..."))

                elif progressBarValue < 85:
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Almost done...."))

                        # Change loadingstatus text
                        QtCore.QTimer.singleShot(0, lambda: self.ui.loadingstatus.setText("QT Project Creator"))

                #increase progressBarValue by 1 after every time interval we set of 100 milliseconds;
                progressBarValue+=1

        def showMainWindow(self):
                self.main = MainAppWindow()
                self.main.show()


# Execute app
# 
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = SplashWindow()
        sys.exit(app.exec_())

