import bcrypt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.Signin import Ui_MainWindow
from model.dao.LoginDAO import LoginDao
from PyQt5.QtCore import pyqtSignal


class SignUpAdmin_controller(QWidget):
    signUp_successful = pyqtSignal(str) 
    
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

        user_id = self.dao.check_username_existence(username)

        if user_id == 0:
            self.ui.show_error_message("Wrong Password")
        else:
            if username != "":
                self.dao.add_new_user(username, password)
                admin_id = username
                self.window.close()
                self.signUp_successful.emit(admin_id)
                    
