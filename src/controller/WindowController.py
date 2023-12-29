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
        self.first_controller = None
        self.login_controller = None
        self.admin_controller = None
        self.NewProduct_controller = None
        
        self.show_FirstWindow()



    def show_FirstWindow(self):
        self.first_controller = FirstWindowController(self)

    def show_login_controller(self):
        self.login_controller = LoginController(self)

    def show_admin_controller(self):
        self.admin_controller = AdminController(self)

    def show_NewProduct(self):
        self.NewProduct_controller = NewProduct_controller(self)

    def show_Products(self):
        self.product_controller = Product_controller(self)

    def closeAll(self):
        self.app.quit()