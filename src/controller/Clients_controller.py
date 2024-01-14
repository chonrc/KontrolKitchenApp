from PyQt5.QtWidgets import QMainWindow, QApplication
from view.clients import Ui_MainWindow
from Custom_Widgets.Widgets import *
from model.dao.ProductDAO import ProductDAO
from PyQt5.QtCore import pyqtSignal
from model.dao.ClientDAO import ClientDao

class Clients_controller(QWidget):
    new_product_pushed = pyqtSignal(str)
    products_pushed = pyqtSignal(str)
    logout_pushed  = pyqtSignal()
    home_pushed = pyqtSignal(str)

    def __init__(self, window_controller, username):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ProductDAO()
        self.clientdao = ClientDao()
        self.username = username

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Products_bttn.clicked.connect(self.products)

        self.ui.display_clients_sales_summary(self.clientdao.get_clients_sales_summary())

        if username is not None:
            self.ui.label_20.setText(username)

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()
    
    def logout(self):
        self.logout_pushed.emit()

    def newProduct(self):
        self.window.close()
        self.new_product_pushed.emit(self.username)

    def products(self):
        self.window.close()
        self.products_pushed.emit(self.username)

    def home(self):
        self.window.close()
        self.home_pushed.emit(self.username)
    
