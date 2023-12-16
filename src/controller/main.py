import sys
import os

# Obtiene la ruta absoluta al directorio padre de este archivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Obtiene la ruta absoluta al directorio padre de la carpeta actual (es decir, src)
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

# Get the current working directory
current_dir = os.getcwd()

# Define the relative path to your database
db_relative_path = os.path.join(current_dir, 'db')
print("Database is located here: ", db_relative_path)
# Add parent directory(src) to sys.path
sys.path.append(parent_directory)
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from controller.Login_controller import LoginController 
from controller.Admin_controller import AdminController 
from PyQt5.QtWidgets import QMainWindow, QApplication


@pyqtSlot()
def show_admin_window(app):
        admin_controller = AdminController(app)

def main():
    app = QApplication([])
    login_controller = LoginController(app)
    
    

    #login_controller.login_successful.connect(lambda: show_admin_window(app))

    sys.exit(login_controller.app.exec_())
    



if __name__ == "__main__":
    main()



