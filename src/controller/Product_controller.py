from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Products import Ui_MainWindow
from Custom_Widgets.Widgets import *
from model.dao.ProductDAO import ProductDAO
from PyQt5.QtCore import pyqtSignal

class Product_controller(QWidget):

    home_pushed = pyqtSignal(str)
    new_product_pushed = pyqtSignal(str)
    logout_pushed  = pyqtSignal()
    clients_pushed  = pyqtSignal(str)

    def __init__(self, window_controller, username):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ProductDAO()
        self.username = username

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Clients_bttn.clicked.connect(self.clients)

        self.ui.setProducts(self.dao.getAllProducts())


        if username is not None:
            self.ui.label_20.setText(username)

        for product_widget in self.ui.product_widgets:
            product_widget.modify_clicked.connect(self.modifyProduct)
            product_widget.delete_clicked.connect(self.deleteProduct)

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()


    def modifyProduct(self, product_widget):
        product = product_widget.product

        name = product_widget.name_line_edit.text()
        description = product_widget.description_line_edit.text()
        price = float(product_widget.price_line_edit.text())
        quantity = int(product_widget.quantity_line_edit.text())

        self.dao.update_product_by_id(product.getID(), name , description, price , quantity)
        pass

    def deleteProduct(self, product):
        
        self.dao.delete_product_by_id(product.getID())
        self.ui.deleteProductWidget(product)
        pass
    
    def logout(self):
        self.logout_pushed.emit()

    def home(self):
        self.window.close()
        self.home_pushed.emit(self.username)

    def newProduct(self):
        self.window.close()
        self.new_product_pushed.emit(self.username)

    def clients(self):
        self.window.close()
        self.clients_pushed.emit(self.username)