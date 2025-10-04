import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QLocale, QTranslator
from ui.mainwindow import MainWindow


import config

def main():
    app = QApplication(sys.argv)
    
    locale = QLocale.system().name()
    config.locale = locale
    
    if sys.platform == 'win32':
        app_font = QFont('Segoe UI', 9)
        QApplication.setFont(app_font)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())

if (__name__ == '__main__'):
    main()