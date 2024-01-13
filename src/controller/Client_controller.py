from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Client import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO

class ClientController(QWidget):
    logout_pushed  = pyqtSignal()


    def __init__(self, window_controller):
        super().__init__()
        self.dao = ProductDAO()

        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)

        self.ui.setProducts(self.dao.getAllProducts())

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/client.json"})

        self.window.show()


    def logout(self):
        self.window.close()
        self.logout_pushed.emit()

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product['name']} add to cart.")

    def remove_cart(self, product):
        try:
            self.cart.remove(product)
            print(f"{product['name']} delete by cart.")
        except ValueError:
            print(f"{product['name']} not found in cart.")

    def look_cart(self):
        print("Products in the cart:")
        for product in self.cart:
            print(f"{product['name']} - {product['prize']}")

    def select_table(self, number_table):
        self.mesa_seleccionada = number_table
        print(f"Table {number_table}.")

    def make_payment(self):
        print("Payment made successfully.")
        self.finish_payment()

    def finish_payment(self):
        print("Order finalized. Enjoy!")
