import bcrypt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.FirstWindow import Ui_MainWindow
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal

class FirstWindowController(QWidget):
    adminwindow = pyqtSignal()
    clientLoginwindow = pyqtSignal()

    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller

        
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_User.clicked.connect(self.user)
        self.ui.pushButton_Admin.clicked.connect(self.admin)

        self.window.show()

    def user(self):
        self.window.close()
        self.clientLoginwindow.emit()
        
    def admin(self):
        self.window.close()
        self.adminwindow.emit()