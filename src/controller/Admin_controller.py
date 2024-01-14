from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Admin import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO
from model.dao.ClientDAO import ClientDao
from model.dao.SalesDAO import SalesDAO


class AdminController(QWidget):
    new_product_pushed = pyqtSignal()
    products_pushed = pyqtSignal()
    logout_pushed  = pyqtSignal()
    clients_pushed  = pyqtSignal()
    
    def __init__(self, window_controller, username):
        super().__init__()
        self.dao = ProductDAO()
        self.client_dao = ClientDao()
        self.sales_dao =  SalesDAO()

        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Products_bttn.clicked.connect(self.products)
        self.ui.Lastest_bttn.clicked.connect(self.products)
        self.ui.Clients_bttn.clicked.connect(self.clients)
        self.ui.MoreClients_bttn.clicked.connect(self.clients)

        if username is not None:
            self.ui.label_20.setText(username)

        self.ui.label_beneficio.setText(str(self.sales_dao.get_total_benefit()))
        self.ui.label_ventas.setText(str(self.sales_dao.get_number_of_sales()))
        self.ui.label_total_products.setText(str(self.dao.get_number_of_products()))
        self.ui.label_total_clientes.setText(str(self.client_dao.get_number_of_clients()))
        self.ui.display_products(self.dao.get_products_dto())
        self.ui.display_clients(self.client_dao.get_clients_list())


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

    def clients(self):
        self.window.close()
        self.clients_pushed.emit()