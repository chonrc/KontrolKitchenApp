from PyQt5.QtWidgets import QApplication, QWidget
from controller.Login_controller import LoginController
from controller.Admin_controller import AdminController
from controller.NewProduct_controller import NewProduct_controller
from controller.FirstWindowController import FirstWindowController
from controller.Product_controller import Product_controller
from controller.ClientLogin_controller import ClientLoginController
from controller.Client_controller import ClientController
from controller.Clients_controller import Clients_controller
from controller.SignUpAdmin_controller import SignUpAdmin_controller

from controller.Cart_controller import CartController

class WindowController:
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.show_first_window()

    def show_first_window(self):
        self.first_controller = FirstWindowController(self)
        self.first_controller.adminwindow.connect(self.show_login_controller)
        self.first_controller.clientLoginwindow.connect(self.show_clientLogin)

    def show_login_controller(self):
        self.login_controller = LoginController(self)
        self.login_controller.login_successful.connect(self.show_admin_controller)
        self.login_controller.newAdmin.connect(self.show_signUpAdmin)


    def show_admin_controller(self, username = None):
        self.admin_controller = AdminController(self, username)
        self.admin_controller.logout_pushed.connect(self.close_all)
        self.admin_controller.new_product_pushed.connect(self.show_new_product)
        self.admin_controller.products_pushed.connect(self.show_products)
        self.admin_controller.clients_pushed.connect(self.show_clients)

    def show_new_product(self, username = None):
        self.new_product_controller = NewProduct_controller(self, username)
        self.new_product_controller.logout_pushed.connect(self.close_all)
        self.new_product_controller.home_pushed.connect(self.show_admin_controller)
        self.new_product_controller.products_pushed.connect(self.show_products)
        self.new_product_controller.clients_pushed.connect(self.show_clients)

    def show_products(self, username = None):
        self.product_controller = Product_controller(self, username)
        self.product_controller.logout_pushed.connect(self.close_all)
        self.product_controller.home_pushed.connect(self.show_admin_controller)
        self.product_controller.new_product_pushed.connect(self.show_new_product)
        self.product_controller.clients_pushed.connect(self.show_clients)

    def show_clientLogin(self):
        self.clientlogin_controller = ClientLoginController(self)
        self.clientlogin_controller.login_successful.connect(self.show_clientMain)


    def show_signUpAdmin(self):
        self.SignUpAdmin_controller = SignUpAdmin_controller(self)
        self.SignUpAdmin_controller.signUp_successful.connect(self.show_admin_controller)


    def show_clientMain(self, client_dto= None):
        self.clientMain = ClientController(self)
        self.clientMain.logout_pushed.connect(self.show_first_window)
        self.clientMain.cart_pushed.connect(self.show_cartWindow)
        self.clientMain.setClient(client_dto)
        
    def show_cartWindow(self, cart):
        self.Cart_controller = CartController(self, cart)
        self.Cart_controller.logout_pushed.connect(self.show_first_window)
        self.Cart_controller.client_pushed.connect(self.show_clientMain)

    def show_clients(self, username = None):
        self.clients = Clients_controller(self, username)
        self.clients.logout_pushed.connect(self.close_all)
        self.clients.new_product_pushed.connect(self.show_new_product)
        self.clients.products_pushed.connect(self.show_products)
        self.clients.home_pushed.connect(self.show_admin_controller)

    def close_all(self):
        self.app.quit()