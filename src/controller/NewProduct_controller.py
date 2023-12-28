from PyQt5.QtWidgets import QMainWindow, QApplication
from view.NewProduct import Ui_MainWindow
from Custom_Widgets.Widgets import *
from model.dao.ProductDAO import ProductDAO

class NewProduct_controller(QWidget):
    def __init__(self, window_controller):
        super().__init__()
        self.window_controller = window_controller
        self.dao = ProductDAO()

        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.ui.pushButton_logout.clicked.connect(self.logout)
        self.ui.home_bttn.clicked.connect(self.home)
        self.ui.check_bttn.clicked.connect(self.submit)
        self.ui.photo_bttn.clicked.connect(self.submit_photo)

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()



    
    def logout(self):
        self.window_controller.closeAll()

    def home(self):
        self.window.close()
        self.window_controller.show_admin_controller()

    def submit(self):
        self.dao.add_new_Product(
            self.ui.ProductName_line.text(),
            self.ui.lineDescription.text(),
            self.ui.doubleSpinBox.value(),
            self.global_blob 
        )

    def submit_photo(self):
        file_name = self.ui.selectPhoto()
        
        if file_name:
            # Read the file and convert it to bytes
            with open(file_name, 'rb') as file:
                file_blob = file.read()

            # Assign the blob to the global variable
            self.global_blob = file_blob
