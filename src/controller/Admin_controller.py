from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Admin import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO

class AdminController(QWidget):
    new_product_pushed = pyqtSignal()
    products_pushed = pyqtSignal()
    logout_pushed  = pyqtSignal()

    def __init__(self, window_controller):
        super().__init__()
        self.dao = ProductDAO()

        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Products_bttn.clicked.connect(self.products)

        self.ui.label_total_products.setText(str(self.dao.get_number_of_products()))
        self.ui.display_products(self.dao.get_products_dto())

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