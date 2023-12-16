import bcrypt
from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Login import Ui_MainWindow
from model.dao.LoginDAO import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class LoginController(QObject):
    
    #login_successful = pyqtSignal()

    def __init__(self, app):
        super().__init__()
        self.model = LoginDao()

        self.app = app
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_Login.clicked.connect(self.login)

        self.window.show()

    def login(self):
        username = self.ui.lineUser.text()
        password = self.ui.linePassword.text()

        admin_service = self.model.check_username_existence(username)

        # Check that an unhashed password matches one that has previously been hashed
        if admin_service is not None and bcrypt.checkpw(password.encode('utf-8'), admin_service.password) and username == admin_service.username:
            print("It Matches!")            
            #self.login_successful.emit()
            self.window.close() 
        else:
            print("It Does not Match :(")
            self.ui.show_error_message("Wrong Username or Password")

        
    def connect_login_successful(self, slot):
        self.login_successful.connect(slot)
        self.login_successful_connected = True