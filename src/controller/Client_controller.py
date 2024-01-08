from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Admin import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO

class ClienteController(QWidget):
    def __init__(self):
        self.cart = []
        self.mesa_seleccionada = None

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

cliente = ClienteController()

cliente.add_to_cart({"id": 1, "name": "Hamburguesa", "precio": 10.99})
cliente.add_to_cart({"id": 2, "name": "Refresco", "precio": 2.5})
cliente.look_cart()
cliente.remove_cart({"id": 1, "name": "Hamburguesa", "precio": 10.99})
cliente.look_cart()
cliente.select_table(5)
cliente.make_payment()
