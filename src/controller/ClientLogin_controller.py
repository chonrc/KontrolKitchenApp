import bcrypt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.Login import Ui_MainWindow
from model.dao.ClientDAO import ClientDao
from PyQt5.QtCore import pyqtSignal

from model.dto.ClientDTO import ClientDTO

class ClientLoginController(QWidget):
    login_successful = pyqtSignal(ClientDTO) 
    
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

        user_id = self.dao.check_username_existence(username, password)

        if user_id == 0:
            self.ui.show_error_message("Wrong Password")
        else:
            client_dto = ClientDTO(username=username, user_id=user_id)

            self.window.close()
            self.login_successful.emit(client_dto)
            
