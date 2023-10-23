########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
try:
    from ui_themepreview import *
except ImportError:
    # print error message
    print(sys.exc_info()[1])
    try:
        from .ui_themepreview import *
    except ImportError:
        print("ERROR: Cannot import UI file")
        # print import error message
        print(sys.exc_info()[1])
        sys.exit()
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################



########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.QSSFolder = os.path.join(os.path.dirname(__file__), "QSS")
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # Get absolute path of the style.json file
        jsonFile = os.path.join(os.path.dirname(__file__), "style.json")
        # print(jsonFile)
        loadJsonStyle(self, self.ui, jsonFiles={
            jsonFile
        })
        ########################################################################

        QAppSettings.updateAppSettings(self)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        # self.show() 
        #######################################################################

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class

        # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        # INITIALIZE APP SETTINGS
        settings = QSettings()
        settings.setValue("THEME", "Default-Theme")
        QAppSettings.updateAppSettings(self)



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
