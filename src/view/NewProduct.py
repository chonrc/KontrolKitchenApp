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
        self.ClientMode_bttn = QtWidgets.QPushButton(self.frame_12)
        self.ClientMode_bttn.setStyleSheet("padding: 10px 5px;\n"
"\n"
"text-align:left;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClientMode_bttn.setIcon(icon4)
        self.ClientMode_bttn.setObjectName("ClientMode_bttn")
        self.verticalLayout_15.addWidget(self.ClientMode_bttn)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Button.setIcon(icon5)
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_Button.setIcon(icon6)
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
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setStyleSheet("background-color: white;\n"
"border-radius:20px")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_5 = QtWidgets.QFrame(self.widget_6)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.clear_bttn = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_bttn.sizePolicy().hasHeightForWidth())
        self.clear_bttn.setSizePolicy(sizePolicy)
        self.clear_bttn.setStyleSheet("border-radius: 10px;\n"
"border: none;\n"
"background-color: rgb(37, 150, 190);")
        self.clear_bttn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_bttn.setIcon(icon7)
        self.clear_bttn.setIconSize(QtCore.QSize(24, 24))
        self.clear_bttn.setObjectName("clear_bttn")
        self.horizontalLayout_13.addWidget(self.clear_bttn)
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.check_bttn = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_bttn.sizePolicy().hasHeightForWidth())
        self.check_bttn.setSizePolicy(sizePolicy)
        self.check_bttn.setStyleSheet("border-radius: 10px;\n"
"border: none;\n"
"background-color: rgb(37, 150, 190);")
        self.check_bttn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/whiteIcons/resources/icons_white/check-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_bttn.setIcon(icon8)
        self.check_bttn.setIconSize(QtCore.QSize(24, 24))
        self.check_bttn.setObjectName("check_bttn")
        self.horizontalLayout_13.addWidget(self.check_bttn)
        self.verticalLayout_9.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.widget_6)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/pen-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile_bttn.setIcon(icon9)
        self.Profile_bttn.setObjectName("Profile_bttn")
        self.verticalLayout_18.addWidget(self.Profile_bttn)
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_13)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/blueIcons/resources/icons_blue/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon10)
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
        self.ClientMode_bttn.setText(_translate("MainWindow", "Client Mode"))
        self.label.setText(_translate("MainWindow", "Dashboard"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search Something"))
        self.label_15.setText(_translate("MainWindow", "New Product"))
        self.label_20.setText(_translate("MainWindow", "AdminName"))
        self.label_19.setText(_translate("MainWindow", "Admin"))
        self.Profile_bttn.setText(_translate("MainWindow", "My Profile"))
        self.pushButton_logout.setText(_translate("MainWindow", " Logout"))

