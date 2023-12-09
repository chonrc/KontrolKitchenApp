import sys
import os

# Obtiene la ruta absoluta al directorio padre de este archivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Obtiene la ruta absoluta al directorio padre de la carpeta actual (es decir, src)
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

# Agrega el directorio padre (src) al sys.path
sys.path.append(parent_directory)

# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from view import Login


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
