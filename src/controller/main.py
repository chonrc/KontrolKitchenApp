import sys
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

# Get the current working directory
current_dir = os.getcwd()

# Define the relative path to your database
db_relative_path = os.path.join(current_dir, 'db')
print("Database is located here: ", db_relative_path)
sys.path.append(parent_directory)
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from controller.Login_controller import LoginController 
from controller.Admin_controller import AdminController 
from controller.WindowController import WindowController
from PyQt5.QtWidgets import QMainWindow, QApplication


def main():
    app = QApplication([])
    window_controller = WindowController(app)
    app.exec_()
    



if __name__ == "__main__":
    main()



