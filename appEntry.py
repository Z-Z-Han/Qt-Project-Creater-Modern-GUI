from splash import SplashWindow
from main import MainWindow

# import QApplication
from PySide2.QtWidgets import QApplication
# import sys
import sys

# Create main class
class AppEntry(QApplication):
    def __init__(self, args):
        QApplication.__init__(self, args)
        self.splash = SplashWindow()
        self.splash.show()
        self.main = MainWindow()
        self.exec_()

# Create if __name__ == '__main__'
if __name__ == '__main__':
    # Create AppEntry class
    app = AppEntry(sys.argv)
    # Execute main class
    sys.exit(app.exec_())
