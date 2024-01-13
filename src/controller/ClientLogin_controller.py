import bcrypt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.Login import Ui_MainWindow
from model.dao.ClientDAO import ClientDao
from PyQt5.QtCore import pyqtSignal

class ClientLoginController(QWidget):
    login_successful = pyqtSignal()


    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ClientDao()

        
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_Login.clicked.connect(self.login)

        self.window.show()

    def login(self):
        username = self.ui.lineUser.text()
        password = self.ui.linePassword.text()

        result = self.dao.check_username_existence(username, password)   

        if result == 0 : 
            self.ui.show_error_message("Wrong Password")

        else:
            self.window.close() 
            self.login_successful.emit() 
