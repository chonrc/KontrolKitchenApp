
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
print("Module Search Path:", sys.path)
import os
print("Current working directory:", os.getcwd())
from view.Login import *




def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
