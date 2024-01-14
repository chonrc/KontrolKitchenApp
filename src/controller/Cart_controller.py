from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from view.Cart import Ui_MainWindow
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import pyqtSignal
from model.dao.ProductDAO import ProductDAO
from model.dao.SalesDAO import SalesDAO
from model.dto.ClientDTO import ClientDTO
from model.entities.Cart import Cart
import random


class CartController(QWidget):
    logout_pushed = pyqtSignal()
    client_pushed = pyqtSignal()
    
    def __init__(self, window_controller, cart):
        super().__init__()
        self.dao = ProductDAO()
        self.salesDAO = SalesDAO()


        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.myCart = cart 
        self.ui.label_20.setText(self.myCart.getClient().get_username())

        self.ui.displayCart(cart)
        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.menu_Button.clicked.connect(self.clientMain)
        self.ui.deleteButton.clicked.connect(self.clear)
        self.ui.payButton.clicked.connect(self.checkOut)
        loadJsonStyle(self, self.ui, jsonFiles={"src/view/client.json"})

        self.window.show()

    def clientMain(self):
        self.window.close()
        self.client_pushed.emit()

    def logout(self):
        self.window.close()
        self.logout_pushed.emit()

    def clear(self):
        self.myCart.clearCart()
        self.ui.displayCart(self.myCart)

    def checkOut(self):
        self.dao.subtract_quantity(self.myCart.getCartItems())

        self.myCart.receipt()

        table_number = random.randint(1, 20)
        print(self.myCart.getClient().get_id())
        self.salesDAO.add_sale(self.myCart.getClient().get_id(), self.myCart.getTotal(), table_number)
        self.logout()
