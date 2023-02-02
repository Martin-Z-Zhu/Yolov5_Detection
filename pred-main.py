# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/cheruichang/Desktop/fitting_detection.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1266, 929)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.camera_frame = QtWidgets.QFrame(self.centralwidget)
        self.camera_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_frame.setObjectName("camera_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.camera_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.camera_frame)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber_2.setFont(font)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_3.addWidget(self.lcdNumber_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.Camera_Display = QtWidgets.QWidget(self.camera_frame)
        self.Camera_Display.setMinimumSize(QtCore.QSize(320, 320))
        self.Camera_Display.setMouseTracking(True)
        self.Camera_Display.setObjectName("Camera_Display")
        self.verticalLayout_2.addWidget(self.Camera_Display)
        self.Take_Image = QtWidgets.QPushButton(self.camera_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Take_Image.sizePolicy().hasHeightForWidth())
        self.Take_Image.setSizePolicy(sizePolicy)
        self.Take_Image.setMinimumSize(QtCore.QSize(0, 30))
        self.Take_Image.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Take_Image.setObjectName("Take_Image")
        self.verticalLayout_2.addWidget(self.Take_Image)
        self.gridLayout_2.addWidget(self.camera_frame, 1, 0, 1, 1)
        self.information_frame = QtWidgets.QFrame(self.centralwidget)
        self.information_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.information_frame.setObjectName("information_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.information_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.information_frame)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.equipment_model_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equipment_model_label.setFont(font)
        self.equipment_model_label.setObjectName("equipment_model_label")
        self.gridLayout_3.addWidget(self.equipment_model_label, 7, 0, 1, 1)
        self.equipment_type_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_type_label.sizePolicy().hasHeightForWidth())
        self.equipment_type_label.setSizePolicy(sizePolicy)
        self.equipment_type_label.setMinimumSize(QtCore.QSize(0, 30))
        self.equipment_type_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equipment_type_label.setFont(font)
        self.equipment_type_label.setObjectName("equipment_type_label")
        self.gridLayout_3.addWidget(self.equipment_type_label, 5, 0, 1, 1)
        self.fitting_input_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_input_txt.sizePolicy().hasHeightForWidth())
        self.fitting_input_txt.setSizePolicy(sizePolicy)
        self.fitting_input_txt.setMinimumSize(QtCore.QSize(0, 30))
        self.fitting_input_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fitting_input_txt.setFont(font)
        self.fitting_input_txt.setObjectName("fitting_input_txt")
        self.gridLayout_3.addWidget(self.fitting_input_txt, 1, 1, 1, 1)
        self.equipment_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_txt.sizePolicy().hasHeightForWidth())
        self.equipment_txt.setSizePolicy(sizePolicy)
        self.equipment_txt.setMinimumSize(QtCore.QSize(0, 30))
        self.equipment_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        self.equipment_txt.setReadOnly(True)
        self.equipment_txt.setObjectName("equipment_txt")
        self.gridLayout_3.addWidget(self.equipment_txt, 5, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.current_ID = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_ID.sizePolicy().hasHeightForWidth())
        self.current_ID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.current_ID.setFont(font)
        self.current_ID.setObjectName("current_ID")
        self.gridLayout_3.addWidget(self.current_ID, 0, 0, 1, 1)
        self.manufacturer_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_txt.sizePolicy().hasHeightForWidth())
        self.manufacturer_txt.setSizePolicy(sizePolicy)
        self.manufacturer_txt.setMinimumSize(QtCore.QSize(0, 30))
        self.manufacturer_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        self.manufacturer_txt.setReadOnly(True)
        self.manufacturer_txt.setObjectName("manufacturer_txt")
        self.gridLayout_3.addWidget(self.manufacturer_txt, 3, 1, 1, 1)
        self.location_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_input_label.sizePolicy().hasHeightForWidth())
        self.location_input_label.setSizePolicy(sizePolicy)
        self.location_input_label.setMinimumSize(QtCore.QSize(0, 30))
        self.location_input_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.location_input_label.setFont(font)
        self.location_input_label.setObjectName("location_input_label")
        self.gridLayout_3.addWidget(self.location_input_label, 9, 0, 1, 1)
        self.manufacturer_list = QtWidgets.QListView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_list.sizePolicy().hasHeightForWidth())
        self.manufacturer_list.setSizePolicy(sizePolicy)
        self.manufacturer_list.setObjectName("manufacturer_list")
        self.gridLayout_3.addWidget(self.manufacturer_list, 4, 1, 1, 1)
        self.hose_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hose_input_label.sizePolicy().hasHeightForWidth())
        self.hose_input_label.setSizePolicy(sizePolicy)
        self.hose_input_label.setMinimumSize(QtCore.QSize(0, 30))
        self.hose_input_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hose_input_label.setFont(font)
        self.hose_input_label.setObjectName("hose_input_label")
        self.gridLayout_3.addWidget(self.hose_input_label, 2, 0, 1, 1)
        self.fitting_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_input_label.sizePolicy().hasHeightForWidth())
        self.fitting_input_label.setSizePolicy(sizePolicy)
        self.fitting_input_label.setMinimumSize(QtCore.QSize(0, 30))
        self.fitting_input_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fitting_input_label.setFont(font)
        self.fitting_input_label.setObjectName("fitting_input_label")
        self.gridLayout_3.addWidget(self.fitting_input_label, 1, 0, 1, 1)
        self.manufacturer_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.manufacturer_label.setFont(font)
        self.manufacturer_label.setObjectName("manufacturer_label")
        self.gridLayout_3.addWidget(self.manufacturer_label, 3, 0, 1, 1)
        self.equipment_list = QtWidgets.QListView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_list.sizePolicy().hasHeightForWidth())
        self.equipment_list.setSizePolicy(sizePolicy)
        self.equipment_list.setObjectName("equipment_list")
        self.gridLayout_3.addWidget(self.equipment_list, 6, 1, 1, 1)
        self.hose_input_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hose_input_txt.sizePolicy().hasHeightForWidth())
        self.hose_input_txt.setSizePolicy(sizePolicy)
        self.hose_input_txt.setMinimumSize(QtCore.QSize(0, 30))
        self.hose_input_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.hose_input_txt.setFont(font)
        self.hose_input_txt.setObjectName("hose_input_txt")
        self.gridLayout_3.addWidget(self.hose_input_txt, 2, 1, 1, 1)
        self.model_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_txt.sizePolicy().hasHeightForWidth())
        self.model_txt.setSizePolicy(sizePolicy)
        self.model_txt.setMinimumSize(QtCore.QSize(0, 30))
        self.model_txt.setMaximumSize(QtCore.QSize(16777215, 30))
        self.model_txt.setReadOnly(True)
        self.model_txt.setObjectName("model_txt")
        self.gridLayout_3.addWidget(self.model_txt, 7, 1, 1, 1)
        self.model_list = QtWidgets.QListView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_list.sizePolicy().hasHeightForWidth())
        self.model_list.setSizePolicy(sizePolicy)
        self.model_list.setObjectName("model_list")
        self.gridLayout_3.addWidget(self.model_list, 8, 1, 1, 1)
        self.locations = QtWidgets.QComboBox(self.widget)
        self.locations.setObjectName("locations")
        self.gridLayout_3.addWidget(self.locations, 9, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.button_frame = QtWidgets.QFrame(self.information_frame)
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.button_frame)
        self.gridLayout_2.addWidget(self.information_frame, 1, 1, 1, 1)
        self.Information_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Information_Label.sizePolicy().hasHeightForWidth())
        self.Information_Label.setSizePolicy(sizePolicy)
        self.Information_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Information_Label.setFont(font)
        self.Information_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Information_Label.setObjectName("Information_Label")
        self.gridLayout_2.addWidget(self.Information_Label, 0, 1, 1, 1)
        self.Camera_Feed_Label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Camera_Feed_Label.sizePolicy().hasHeightForWidth())
        self.Camera_Feed_Label.setSizePolicy(sizePolicy)
        self.Camera_Feed_Label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Camera_Feed_Label.setFont(font)
        self.Camera_Feed_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Camera_Feed_Label.setObjectName("Camera_Feed_Label")
        self.gridLayout_2.addWidget(self.Camera_Feed_Label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1266, 24))
        self.menubar.setObjectName("menubar")
        self._Menu = QtWidgets.QMenu(self.menubar)
        self._Menu.setObjectName("_Menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self._Storage = QtWidgets.QAction(MainWindow)
        self._Storage.setObjectName("_Storage")
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self._Menu.addAction(self._Storage)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self._Menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "No. of Fittings Detected:"))
        self.Take_Image.setText(_translate("MainWindow", "Take Image"))
        self.equipment_model_label.setText(_translate("MainWindow", "Equipment Model"))
        self.equipment_type_label.setText(_translate("MainWindow", "Equipment Type:"))
        self.current_ID.setText(_translate("MainWindow", "Currently Selected:"))
        self.location_input_label.setText(_translate("MainWindow", "Location:"))
        self.hose_input_label.setText(_translate("MainWindow", "Hose Type:"))
        self.fitting_input_label.setText(_translate("MainWindow", "Fitting Type:"))
        self.manufacturer_label.setText(_translate("MainWindow", "Manufacturer"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_3.setText(_translate("MainWindow", "Skip"))
        self.pushButton_2.setText(_translate("MainWindow", "Submit"))
        self.Information_Label.setText(_translate("MainWindow", "Information"))
        self.Camera_Feed_Label.setText(_translate("MainWindow", "Camera Feed"))
        self._Menu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self._Storage.setText(_translate("MainWindow", "Storage"))
        self.actionManual.setText(_translate("MainWindow", "How to Use"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
