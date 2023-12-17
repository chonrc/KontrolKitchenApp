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

        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()

    def logout(self):
        self.window_controller.closeAll()

