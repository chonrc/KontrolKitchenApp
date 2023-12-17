from PyQt5.QtWidgets import QMainWindow, QApplication
from view.NewProduct import Ui_MainWindow
from Custom_Widgets.Widgets import *

class NewProduct_controller(QWidget):
    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()

    def logout(self):
        self.window_controller.closeAll()

    def home(self):
        self.window.close()
        self.window_controller.show_admin_controller()