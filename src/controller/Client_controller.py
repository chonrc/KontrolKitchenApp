from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Client import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO
from model.entities.Cart import Cart

class ClientController(QWidget):
    logout_pushed  = pyqtSignal()
    cart_pushed = pyqtSignal(Cart)
    myCart = Cart()

    def __init__(self, window_controller):
        super().__init__()
        self.dao = ProductDAO()

        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)


        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.menu_Button.clicked.connect(self.cartwindow)
        self.ui.setProducts(self.dao.getAllProducts())

        for product_widget in self.ui.product_widgets:
            product_widget.add_to_cart_clicked.connect(self.add_to_cart)
            

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/client.json"})

        self.window.show()


    def setClient(self, client_dto):
        if client_dto is not None:
            self.myCart.setClient(client_dto)

        self.ui.label_20.setText(self.myCart.getClient().get_username())

        
    def logout(self):
        self.window.close()
        self.logout_pushed.emit()

    def cartwindow(self):
        self.window.close()
        self.cart_pushed.emit(self.myCart)

    def add_to_cart(self, product):
        self.myCart.addProduct(product)
        print("added to cart.")








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
