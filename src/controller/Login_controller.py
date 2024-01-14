import bcrypt
from PyQt5.QtWidgets import QMainWindow, QWidget
from view.Login_Admin import Ui_MainWindow
from model.dao.LoginDAO import LoginDao
from PyQt5.QtCore import pyqtSignal

class LoginController(QWidget):
    login_successful = pyqtSignal(str)


    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.dao = LoginDao()

        
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_Login.clicked.connect(self.login)

        self.window.show()

    def login(self):
        username = self.ui.lineUser.text()
        password = self.ui.linePassword.text()

        admin_service = self.dao.check_username_existence(username)

        # Check that an unhashed password matches one that has previously been hashed
        if admin_service is not None and bcrypt.checkpw(password.encode('utf-8'), admin_service.password) and username == admin_service.username:
            print("It Matches!")            
            self.window.close() 
            self.login_successful.emit(username) 
        else:
            print("It Does not Match :(")
            self.ui.show_error_message("Wrong Username or Password")
