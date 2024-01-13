from PyQt5 import QtCore, QtGui, QtWidgets
from Custom_Widgets.Widgets import QCustomSlideMenu


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
        self.menu_Button.setStyleSheet("background-color: rgb(239, 249, 254);\n"
"border: none;\n"
"")
        self.menu_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/arrow-left-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Button.setIcon(icon)
        self.menu_Button.setIconSize(QtCore.QSize(32, 32))
        self.menu_Button.setObjectName("menu_Button")
        self.horizontalLayout_3.addWidget(self.menu_Button)
        self.horizontalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignLeft)
        self.deleteButton = QtWidgets.QPushButton(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(239, 249, 254);\n"
"border: none;\n"
"color: rgb(37, 150, 190);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/slash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(32, 32))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.payButton = QtWidgets.QPushButton(self.headerFrame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.payButton.setFont(font)
        self.payButton.setStyleSheet("background-color: rgb(239, 249, 254);\n"
"border: none;\n"
"color: rgb(37, 150, 190);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/thumbs-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.payButton.setIcon(icon2)
        self.payButton.setIconSize(QtCore.QSize(32, 32))
        self.payButton.setObjectName("payButton")
        self.horizontalLayout_2.addWidget(self.payButton)
        self.widget_5 = QtWidgets.QWidget(self.headerFrame)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.account_Button = QtWidgets.QPushButton(self.widget_5)
        self.account_Button.setStyleSheet("border: none;")
        self.account_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Button.setIcon(icon3)
        self.account_Button.setIconSize(QtCore.QSize(32, 32))
        self.account_Button.setObjectName("account_Button")
        self.horizontalLayout_5.addWidget(self.account_Button)
        self.horizontalLayout_2.addWidget(self.widget_5, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerFrame)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/pen-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile_bttn.setIcon(icon4)
        self.Profile_bttn.setObjectName("Profile_bttn")
        self.verticalLayout_18.addWidget(self.Profile_bttn)
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_13)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon5)
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
        self.deleteButton.setText(_translate("MainWindow", "Delete Cart "))
        self.payButton.setText(_translate("MainWindow", "Pay"))
        self.label_20.setText(_translate("MainWindow", "ClientName"))
        self.label_19.setText(_translate("MainWindow", "Client"))
        self.Profile_bttn.setText(_translate("MainWindow", "My Profile"))
        self.pushButton_logout.setText(_translate("MainWindow", " Logout"))
   
   
   
    def displayCart(self, cart):
        # Clear frame 6
        self.clearFrame()

        # Iterate through the items in the cart and display them
        for item in cart.getCartItems():
                product = item['product']
                quantity = item['quantity']

                productWidget = QtWidgets.QWidget(self.frame_6)
                productWidget.setObjectName("productWidget")
                productLayout = QtWidgets.QHBoxLayout(productWidget)
                productLayout.setObjectName("productLayout")

                productNameLabel = QtWidgets.QLabel(productWidget)
                productNameLabel.setText(product.getName())
                productLayout.addWidget(productNameLabel)

                quantityLabel = QtWidgets.QLabel(productWidget)
                quantityLabel.setText(f"Quantity: {quantity}")
                productLayout.addWidget(quantityLabel)

                priceLabel = QtWidgets.QLabel(productWidget)
                priceLabel.setText(f"Price: ${product.getPrice() * quantity:.2f}")
                productLayout.addWidget(priceLabel)

                plusButton = QtWidgets.QPushButton(productWidget)
                plusButton.setText("+")
                plusButton.clicked.connect(lambda _, p=product: self.adjustQuantity(cart, p, 1))
                self.styleButton(plusButton)
                productLayout.addWidget(plusButton)

                minusButton = QtWidgets.QPushButton(productWidget)
                minusButton.setText("-")
                minusButton.clicked.connect(lambda _, p=product: self.adjustQuantity(cart, p, -1))
                self.styleButton(minusButton, is_plus=False)
                productLayout.addWidget(minusButton)

                self.verticalLayout_2.addWidget(productWidget)

        # Display total with improved visibility
        totalLabel = QtWidgets.QLabel(self.frame_6)
        totalLabel.setText(f"Total: ${cart.getTotal():.2f}")
        self.styleTotalLabel(totalLabel)
        self.verticalLayout_2.addWidget(totalLabel)

    def clearFrame(self):
        # Clear frame 6
        for i in reversed(range(self.verticalLayout_2.count())):
                widgetToRemove = self.verticalLayout_2.takeAt(i).widget()
                if widgetToRemove is not None:
                        widgetToRemove.setParent(None)


                        
    def styleButton(self, button, is_plus=True):
        # Apply styling to + and - buttons
        color = "#4CAF50" if is_plus else "#FF0000"  # Green for +, Red for -
        button.setStyleSheet(f"""
                QPushButton {{
                background-color: {color};
                color: white;
                border: 1px solid {color};
                border-radius: 5px;
                padding: 5px;
                }}
                QPushButton:hover {{
                background-color: #45a049;
                }}
        """)

    def styleTotalLabel(self, label):
        # Apply styling to the total label
        label.setStyleSheet("""
                QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                }
        """)

    def adjustQuantity(self, cart, product, change):
        for item in cart.getCartItems():
            if item['product'].getID() == product.getID():
                item['quantity'] += change

        self.displayCart(cart)