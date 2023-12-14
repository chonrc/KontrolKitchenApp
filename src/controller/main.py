import sys
import os

# Obtiene la ruta absoluta al directorio padre de este archivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Obtiene la ruta absoluta al directorio padre de la carpeta actual (es decir, src)
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

# Agrega el directorio padre (src) al sys.path
sys.path.append(parent_directory)

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Custom_Widgets.Widgets import *
from view.Admin import *  # Replace 'your_module_name' with the actual module name
from view.Login import * 

class MyApplication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #loadJsonStyle(self, self.ui, jsonFiles = { "src/view/style.json"})
        self.show()  
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyApplication()
    mainWindow.show()
    sys.exit(app.exec_())

