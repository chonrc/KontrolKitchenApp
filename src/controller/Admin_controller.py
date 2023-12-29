from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Admin import Ui_MainWindow
from Custom_Widgets.Widgets import *

class AdminController(QWidget):
    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)
        self.ui.Products_bttn.clicked.connect(self.products)

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()

    def logout(self):
        self.window_controller.closeAll()

    def newProduct(self):
        self.window.close()
        self.window_controller.show_NewProduct()

    def products(self):
        self.window.close()
        self.window_controller.show_Products()