from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Cart import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO
from model.entities.Cart import Cart

class CartController(QWidget):
    logout_pushed  = pyqtSignal()
    client_pushed = pyqtSignal()
    myCart = Cart()

    def __init__(self, window_controller):
        super().__init__()
        self.dao = ProductDAO()

        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)


        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.menu_Button.clicked.connect(self.clientMain)


        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/client.json"})

        self.window.show()




    
    def clientMain(self):
        self.window.close()
        self.client_pushed.emit()


    def logout(self):
        self.window.close()
        self.logout_pushed.emit()