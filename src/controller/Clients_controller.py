from PyQt5.QtWidgets import QMainWindow, QApplication
from view.clients import Ui_MainWindow
from Custom_Widgets.Widgets import *
from model.dao.ProductDAO import ProductDAO
from PyQt5.QtCore import pyqtSignal
from model.dao.ClientDAO import ClientDao

class Clients_controller(QWidget):
    new_product_pushed = pyqtSignal()
    products_pushed = pyqtSignal()
    logout_pushed  = pyqtSignal()
    home_pushed = pyqtSignal()

    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ProductDAO()
        self.clientdao = ClientDao()

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Products_bttn.clicked.connect(self.products)

        self.ui.display_clients_sales_summary(self.clientdao.get_clients_sales_summary())


        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()
    
    def logout(self):
        self.logout_pushed.emit()

    def newProduct(self):
        self.window.close()
        self.new_product_pushed.emit()

    def products(self):
        self.window.close()
        self.products_pushed.emit()

    def home(self):
        self.window.close()
        self.home_pushed.emit()
    
