

from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import QCustomSlideMenu
from PyQt5.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QHBoxLayout,  QLabel, QLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
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
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setMinimumSize(QtCore.QSize(230, 0))
        self.leftMenu.setMaximumSize(QtCore.QSize(230, 16777215))
        self.leftMenu.setStyleSheet("background-color: rgb(37, 150, 190);\n"
"border: none;")
        self.leftMenu.setObjectName("leftMenu")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.leftMenu)
        self.verticalLayout_11.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_9 = QtWidgets.QFrame(self.leftMenu)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.home_bttn = QtWidgets.QPushButton(self.frame_12)
        self.home_bttn.setStyleSheet("padding: 10px 5px;\n"
"\n"
"text-align:left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_bttn.setIcon(icon)
        self.home_bttn.setIconSize(QtCore.QSize(24, 24))
        self.home_bttn.setObjectName("home_bttn")
        self.verticalLayout_15.addWidget(self.home_bttn)
        self.Products_bttn = QtWidgets.QPushButton(self.frame_12)
        self.Products_bttn.setStyleSheet("padding: 10px 5px;\n"
"background-color: #fefeff;\n"
"text-align:left;\n"
"border-top-left-radius:20px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/bar-chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Products_bttn.setIcon(icon1)
        self.Products_bttn.setIconSize(QtCore.QSize(24, 24))
        self.Products_bttn.setObjectName("Products_bttn")
        self.verticalLayout_15.addWidget(self.Products_bttn)
        self.NewProduct_bttn = QtWidgets.QPushButton(self.frame_12)
        self.NewProduct_bttn.setStyleSheet("padding: 10px 5px;\n"
"\n"
"text-align:left;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewProduct_bttn.setIcon(icon2)
        self.NewProduct_bttn.setIconSize(QtCore.QSize(24, 24))
        self.NewProduct_bttn.setObjectName("NewProduct_bttn")
        self.verticalLayout_15.addWidget(self.NewProduct_bttn)
        self.Clients_bttn = QtWidgets.QPushButton(self.frame_12)
        self.Clients_bttn.setStyleSheet("padding: 10px 5px;\n"
"\n"
"text-align:left;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Clients_bttn.setIcon(icon3)
        self.Clients_bttn.setIconSize(QtCore.QSize(24, 24))
        self.Clients_bttn.setObjectName("Clients_bttn")
        self.verticalLayout_15.addWidget(self.Clients_bttn)
        self.verticalLayout_16.addWidget(self.frame_12, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.verticalLayout_11.addWidget(self.frame_9)
        self.horizontalLayout.addWidget(self.leftMenu)
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
        self.menu_Button.setStyleSheet("background-color: rgb(239, 249, 254);\n"
"border: none;\n"
"")
        self.menu_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Button.setIcon(icon4)
        self.menu_Button.setIconSize(QtCore.QSize(24, 24))
        self.menu_Button.setObjectName("menu_Button")
        self.horizontalLayout_3.addWidget(self.menu_Button)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(37, 150, 190);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.widget_3 = QtWidgets.QWidget(self.headerFrame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_frame = QtWidgets.QFrame(self.widget_3)
        self.search_frame.setMinimumSize(QtCore.QSize(160, 0))
        self.search_frame.setStyleSheet("border-radius: 10px;\n"
"border: 2px solid rgb(37, 150, 190);")
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.search_frame)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.label_2.setStyleSheet("border: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/search.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.lineEdit.setStyleSheet("background: transparent;\n"
"border: transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.horizontalLayout_4.addWidget(self.search_frame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_5 = QtWidgets.QWidget(self.headerFrame)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.account_Button = QtWidgets.QPushButton(self.widget_5)
        self.account_Button.setStyleSheet("border: none;")
        self.account_Button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Button.setIcon(icon5)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/pen-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile_bttn.setIcon(icon6)
        self.Profile_bttn.setObjectName("Profile_bttn")
        self.verticalLayout_18.addWidget(self.Profile_bttn)
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_13)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon7)
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
        self.label_17.setText(_translate("MainWindow", "KitchenKontrol"))
        self.home_bttn.setText(_translate("MainWindow", "Home"))
        self.Products_bttn.setText(_translate("MainWindow", "Products"))
        self.NewProduct_bttn.setText(_translate("MainWindow", "Add Product"))
        self.Clients_bttn.setText(_translate("MainWindow", "Clients"))
        self.label.setText(_translate("MainWindow", "Dashboard"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search Something"))
        self.label_20.setText(_translate("MainWindow", "AdminName"))
        self.label_19.setText(_translate("MainWindow", "Admin"))
        self.Profile_bttn.setText(_translate("MainWindow", "My Profile"))
        self.pushButton_logout.setText(_translate("MainWindow", " Logout"))
        
    def setProducts(self, products):
        scroll_area = QScrollArea(self.frame_6)
        scroll_area.setWidgetResizable(True)
        
        # Create a widget to hold the products vertically
        scroll_widget = QWidget(scroll_area)
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_widget.setLayout(scroll_layout)

        # Add products to the layout
        for product in products:
            product_widget = ProductWidget(product)
            scroll_layout.addWidget(product_widget)

        # Set the scroll area widget
        scroll_area.setWidget(scroll_widget)

        # Add the scroll area to the main layout
        main_layout = QHBoxLayout(self.frame_6)
        main_layout.addWidget(scroll_area)

        self.frame_6.setLayout(main_layout)


class ProductWidget(QtWidgets.QWidget):
    def __init__(self, product):
        super().__init__()

        # Set the background color
        self.setStyleSheet("background-color: #fefeff; color: black;")

        # Create a container frame with a layout
        container_frame = QtWidgets.QFrame(self)
        container_layout = QtWidgets.QVBoxLayout(container_frame)

        # Set the border style and rounded corners for the container frame
        border_style = "border: 1px solid black; border-radius: 10px;"
        container_frame.setStyleSheet(border_style)

        # Assuming product.image is a bytes object containing image data
        image_data = product.image

        # Check if image_data is not None
        if image_data is not None:
        # Convert bytes to a QByteArray
                qbytearray = QtCore.QByteArray(image_data)

        # Create a QPixmap from the QByteArray
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(qbytearray)

                # Set up the photo_label with the QPixmap
                photo_label = QtWidgets.QLabel()
                photo_label.setPixmap(pixmap)
                container_layout.addWidget(photo_label)
        else:
                # If image_data is None, display a message in the label
                photo_label = QtWidgets.QLabel("There is no photo.")
                container_layout.addWidget(photo_label)

        # Name
        self.name_line_edit = QtWidgets.QLineEdit(product.name)
        self.name_line_edit.setReadOnly(True)
        self.name_line_edit.setStyleSheet("color: black;")  # Set text color to black
        container_layout.addWidget(self.name_line_edit)

        # Description
        self.description_line_edit = QtWidgets.QLineEdit(product.description)
        self.description_line_edit.setReadOnly(True)
        self.description_line_edit.setStyleSheet("color: black;")  # Set text color to black
        container_layout.addWidget(self.description_line_edit)

        # Price
        price_layout = QtWidgets.QHBoxLayout()
        price_label = QtWidgets.QLabel("Price:")
        price_label.setStyleSheet("color: black;")  # Set text color to black
        self.price_line_edit = QtWidgets.QLineEdit(str(product.price))
        self.price_line_edit.setReadOnly(True)
        self.price_line_edit.setStyleSheet("color: black;")  # Set text color to black
        price_layout.addWidget(price_label)
        price_layout.addWidget(self.price_line_edit)
        container_layout.addLayout(price_layout)

        # Quantity
        quantity_layout = QtWidgets.QHBoxLayout()
        quantity_label = QtWidgets.QLabel("Quantity:")
        quantity_label.setStyleSheet("color: black;")  # Set text color to black
        self.quantity_line_edit = QtWidgets.QLineEdit(str(product.quantity))
        self.quantity_line_edit.setReadOnly(True)
        self.quantity_line_edit.setStyleSheet("color: black;")  # Set text color to black
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(self.quantity_line_edit)
        container_layout.addLayout(quantity_layout)

        # Set up the layout for the main widget
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(container_frame)

        self.name_line_edit.setReadOnly(False)
        self.description_line_edit.setReadOnly(False)
        self.price_line_edit.setReadOnly(False)
        self.quantity_line_edit.setReadOnly(False)

        # Set validator to accept only numbers
        price_validator = QtGui.QDoubleValidator(self)
        price_validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.price_line_edit.setValidator(price_validator)

        quantity_validator = QtGui.QIntValidator(self)
        self.quantity_line_edit.setValidator(quantity_validator)

        self.setLayout(main_layout)
