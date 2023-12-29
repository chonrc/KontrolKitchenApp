from PyQt5.QtWidgets import QApplication, QWidget
from controller.Login_controller import LoginController
from controller.Admin_controller import AdminController
from controller.NewProduct_controller import NewProduct_controller
from controller.FirstWindowController import FirstWindowController
from controller.Product_controller import Product_controller

class WindowController:
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.show_first_window()

    def show_first_window(self):
        self.first_controller = FirstWindowController(self)
        self.first_controller.nextwindow.connect(self.show_login_controller)

    def show_login_controller(self):
        self.login_controller = LoginController(self)
        self.login_controller.login_successful.connect(self.show_admin_controller)

    def show_admin_controller(self):
        self.admin_controller = AdminController(self)
        self.admin_controller.logout_pushed.connect(self.close_all)
        self.admin_controller.new_product_pushed.connect(self.show_new_product)
        self.admin_controller.products_pushed.connect(self.show_products)

    def show_new_product(self):
        self.new_product_controller = NewProduct_controller(self)
        self.new_product_controller.logout_pushed.connect(self.close_all)
        self.new_product_controller.home_pushed.connect(self.show_admin_controller)
        self.new_product_controller.products_pushed.connect(self.show_products)

    def show_products(self):
        self.product_controller = Product_controller(self)
        self.product_controller.logout_pushed.connect(self.close_all)
        self.product_controller.home_pushed.connect(self.show_admin_controller)
        self.product_controller.new_product_pushed.connect(self.show_new_product)

    def close_all(self):
        self.app.quit()