from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Products import Ui_MainWindow
from Custom_Widgets.Widgets import *
from model.dao.ProductDAO import ProductDAO

class Product_controller(QWidget):
    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ProductDAO()

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)
        self.ui.NewProduct_bttn.clicked.connect(self.newProduct)

        self.ui.setProducts(self.dao.getAllProducts())
        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()



    
    def logout(self):
        self.window_controller.closeAll()

    def home(self):
        self.window.close()
        self.window_controller.show_admin_controller()

    def newProduct(self):
        self.window.close()
        self.window_controller.show_NewProduct()