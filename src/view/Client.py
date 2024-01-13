
from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import QCustomSlideMenu
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout,  QLabel, QLineEdit, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.product_widgets = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1294, 669)

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
         # Get the screen geometry
        screen_geo = QtWidgets.QDesktopWidget().screenGeometry()

        # Calculate the center position for the main window
        center_x = (screen_geo.width() - MainWindow.width()) // 2
        center_y = (screen_geo.height() - MainWindow.height()) // 2

        # Set the window position to the center
        MainWindow.setGeometry(center_x, center_y, MainWindow.width(), MainWindow.height())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("*{\n"
"    color: #000;\n"
"    border: none;\n"
"}\n"
"#centralwidget{\n"
"    background-color: #eff9fe;\n"
"\n"
"}\n"
" #frame_11{\n"
"    background-color: #2596be;\n"
"}\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    color: #2596be;\n"
"}\n"
"#searchFrame{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2596be;\n"
"}\n"
"#appHeader{\n"
"    color: #2596be;\n"
"}\n"
"#card1, #card2, #card3, #card4 {\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#pushButton, #pushButton_2{\n"
"    background-color: #2596be;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"}\n"
"#widget_4, #widget_5, #profileCont, #frame_15{\n"
"    background-color: #fefeff;\n"
"    border-radius: 20px;\n"
"}\n"
"#headerFrame{\n"
"    background-color: #fefeff;\n"
"}\n"
"#pushButton_3{\n"
"    background-color: #fefeff;\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"    border-top-left-radius: 20px ;\n"
"}\n"
"QPushButton{\n"
"    padding: 10px 5px;\n"
"    text-align: left;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setStyleSheet("background-color: rgb(239, 249, 254);")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QWidget(self.mainBody)
        self.headerFrame.setStyleSheet("")
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.headerFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_Button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.menu_Button.setFont(font)
        self.menu_Button.setStyleSheet("background-color: rgb(239, 249, 254);\n"
"border: none;\n"
"")
        self.menu_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/shopping-cart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Button.setIcon(icon)
        self.menu_Button.setIconSize(QtCore.QSize(32, 32))
        self.menu_Button.setObjectName("menu_Button")
        self.horizontalLayout_3.addWidget(self.menu_Button)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_5 = QtWidgets.QWidget(self.headerFrame)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.account_Button = QtWidgets.QPushButton(self.widget_5)
        self.account_Button.setStyleSheet("border: none;")
        self.account_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Button.setIcon(icon1)
        self.account_Button.setIconSize(QtCore.QSize(32, 32))
        self.account_Button.setObjectName("account_Button")
        self.horizontalLayout_5.addWidget(self.account_Button)
        self.horizontalLayout_2.addWidget(self.widget_5, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.widget_4 = QtWidgets.QWidget(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("background-color: #eff9fe;")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setStyleSheet("background-color: white;\n"
"border-radius:20px;\n"
"background-color: #eff9fe")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_6 = QtWidgets.QFrame(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: #eff9fe;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9.addWidget(self.frame_6)
        self.horizontalLayout_12.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.mainBody)
        self.profileCont = QCustomSlideMenu(self.centralwidget)
        self.profileCont.setMinimumSize(QtCore.QSize(130, 170))
        self.profileCont.setMaximumSize(QtCore.QSize(130, 170))
        self.profileCont.setObjectName("profileCont")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.profileCont)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_13 = QtWidgets.QFrame(self.profileCont)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_13.setStyleSheet("border-radius: 20px;\n"
"background-color:#fefeff;\n"
"padding: 5px 5px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_20 = QtWidgets.QLabel(self.frame_13)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_18.addWidget(self.label_20, 0, QtCore.Qt.AlignTop)
        self.label_19 = QtWidgets.QLabel(self.frame_13)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_18.addWidget(self.label_19, 0, QtCore.Qt.AlignTop)
        self.label_18 = QtWidgets.QLabel(self.frame_13)
        self.label_18.setMinimumSize(QtCore.QSize(50, 50))
        self.label_18.setMaximumSize(QtCore.QSize(50, 50))
        self.label_18.setAutoFillBackground(False)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/images/resources/logo_negro.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter)
        self.Profile_bttn = QtWidgets.QPushButton(self.frame_13)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/pen-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile_bttn.setIcon(icon2)
        self.Profile_bttn.setObjectName("Profile_bttn")
        self.verticalLayout_18.addWidget(self.Profile_bttn)
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_13)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon3)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.verticalLayout_18.addWidget(self.pushButton_logout)
        self.verticalLayout_17.addWidget(self.frame_13, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.profileCont, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "ClientName"))
        self.label_19.setText(_translate("MainWindow", "Client"))
        self.Profile_bttn.setText(_translate("MainWindow", "My Profile"))
        self.pushButton_logout.setText(_translate("MainWindow", " Logout"))
    def setProducts(self, products):
        scroll_area = QScrollArea(self.frame_6)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the products in a grid
        scroll_widget = QWidget(scroll_area)
        scroll_layout = QGridLayout(scroll_widget)
        scroll_widget.setLayout(scroll_layout)

        # Add products to the layout
        for index, product in enumerate(products):
                product_widget = ProductWidget(product)
                row = index // 3  
                column = index % 3
                product_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                scroll_layout.addWidget(product_widget, row, column)
                self.product_widgets.append(product_widget)

        # Set the scroll area widget
        scroll_area.setWidget(scroll_widget)

        # Add the scroll area to the main layout
        main_layout = QHBoxLayout(self.frame_6)
        main_layout.addWidget(scroll_area)

        self.frame_6.setLayout(main_layout)
                

class ProductWidget(QtWidgets.QWidget):
    
   add_to_cart_clicked = QtCore.pyqtSignal(object)

   def __init__(self, product):
        super().__init__()
        self.product = product

        self.setStyleSheet("background-color: #f8f8f8; color: #333;")

        container_frame = QtWidgets.QFrame(self)
        container_frame.setObjectName("productFrame")
        container_layout = QtWidgets.QVBoxLayout(container_frame)
        container_layout.setContentsMargins(10, 10, 10, 10)

        image_data = product.image

        if image_data is not None:
                qbytearray = QtCore.QByteArray(image_data)
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(qbytearray)

                photo_label = QtWidgets.QLabel()
                photo_label.setPixmap(pixmap.scaledToWidth(150))
                photo_label.setAlignment(QtCore.Qt.AlignCenter)
                container_layout.addWidget(photo_label)
        else:
                no_photo_label = QtWidgets.QLabel("No Photo Available")
                no_photo_label.setAlignment(QtCore.Qt.AlignCenter)
                no_photo_label.setStyleSheet("font-style: italic; color: #777;")
                container_layout.addWidget(no_photo_label)

        # Name
        name_label = QtWidgets.QLabel("Name:")
        name_label.setStyleSheet("font-weight: bold; color: #333;")
        container_layout.addWidget(name_label)
        self.name_label = QtWidgets.QLabel(product.name)
        self.name_label.setStyleSheet("color: #333;")
        container_layout.addWidget(self.name_label)

        # Description
        description_label = QtWidgets.QLabel("Description:")
        description_label.setStyleSheet("font-weight: bold; color: #333;")
        container_layout.addWidget(description_label)
        self.description_label = QtWidgets.QLabel(product.description)
        self.description_label.setStyleSheet("color: #333;")
        container_layout.addWidget(self.description_label)

        # Price
        price_label = QtWidgets.QLabel("Price:")
        price_label.setStyleSheet("font-weight: bold; color: #333;")
        container_layout.addWidget(price_label)
        self.price_label = QtWidgets.QLabel(f"${product.price}")
        self.price_label.setStyleSheet("color: #333;")
        container_layout.addWidget(self.price_label)

        # Add to Cart Button
        add_to_cart_button = QtWidgets.QPushButton("Add to Cart")
        add_to_cart_button.setStyleSheet("background-color: #4285f4; color: white;")
        add_to_cart_button.clicked.connect(lambda: self.add_to_cart_clicked.emit(product))
        container_layout.addWidget(add_to_cart_button, alignment=QtCore.Qt.AlignCenter)

        # Set up the layout for the main widget
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(container_frame)

        self.setLayout(main_layout)