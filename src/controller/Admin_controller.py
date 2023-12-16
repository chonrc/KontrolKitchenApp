from PyQt5.QtWidgets import QMainWindow, QApplication
from view.Admin import Ui_MainWindow
from Custom_Widgets.Widgets import *

class AdminController:
    def __init__(self, app):

        self.app = app
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.window.show()