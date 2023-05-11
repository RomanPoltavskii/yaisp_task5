import sys
import os
from MainWindow import MainWindow

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'plugins\Lib\site-packages\PyQt5\Qt5\plugins'

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())