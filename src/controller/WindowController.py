from PyQt5.QtWidgets import QApplication, QWidget
from controller.Login_controller import LoginController
from controller.Admin_controller import AdminController

class WindowController:
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.login_controller = None
        self.admin_controller = None
        self.show_login_controller()

    def show_login_controller(self):
        self.login_controller = LoginController(self)

    def show_admin_controller(self):
        self.admin_controller = AdminController(self)

    def closeAll(self):
        # Close all windows
        if self.login_controller:
            self.login_controller.close()
        if self.admin_controller:
            self.admin_controller.close()

        # Finish the execution
        self.app.quit()