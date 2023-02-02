import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import Default_Thread
import cv2
import datetime
import time
import platform
import os
import subprocess
import numpy as np
from PIL import Image, ImageColor, ImageEnhance
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        f = open('assetDatabase.json')
        self.assets = json.load(f)
        f.close()
        self.manufacturers = self.assets.keys()

        MainWindow.setObjectName("MainWindow")
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
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fitting_count_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.fitting_count_label.setFont(font)
        self.fitting_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fitting_count_label.setObjectName("fitting_count_label")
        self.fitting_count_label.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalLayout_3.addWidget(self.fitting_count_label)
        self.fitting_count_lcd = QtWidgets.QLCDNumber(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_count_lcd.sizePolicy().hasHeightForWidth())
        self.fitting_count_lcd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.fitting_count_lcd.setFont(font)
        self.fitting_count_lcd.setObjectName("fitting_count_lcd")
        self.fitting_count_lcd.setMinimumSize(QtCore.QSize(0, 40))
        self.fitting_count_lcd.setStyleSheet('background-color: white')
        self.horizontalLayout_3.addWidget(self.fitting_count_lcd)
        self.verticalLayout_2.addWidget(self.frame)
        self.Camera_Display = Camera_Display(self.camera_frame, self)
        self.verticalLayout_2.addWidget(self.Camera_Display)
        self.take_image_button = QtWidgets.QPushButton(self.camera_frame)
        self.take_image_button.clicked.connect(self.take_image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.take_image_button.sizePolicy().hasHeightForWidth())
        self.take_image_button.setSizePolicy(sizePolicy)
        self.take_image_button.setMinimumSize(QtCore.QSize(0, 30))
        self.take_image_button.setMaximumSize(QtCore.QSize(16777215, 100))
        self.take_image_button.setObjectName("Take_Image")
        self.take_image_button.setFont(font)
        self.verticalLayout_2.addWidget(self.take_image_button)
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
        font.setPointSize(30)
        self.equipment_model_label.setFont(font)
        self.equipment_model_label.setObjectName("equipment_model_label")
        self.gridLayout_3.addWidget(self.equipment_model_label, 7, 0, 1, 1)

        self.model_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_txt.sizePolicy().hasHeightForWidth())
        self.model_txt.setSizePolicy(sizePolicy)
        self.model_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.model_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        self.model_txt.setReadOnly(True)
        self.model_txt.setObjectName("model_txt")
        self.model_txt.setFont(font)
        self.gridLayout_3.addWidget(self.model_txt, 7, 1, 1, 1)

        self.model_list = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_list.sizePolicy().hasHeightForWidth())
        self.model_list.setSizePolicy(sizePolicy)
        self.model_list.setObjectName("model_list")
        self.model_list.clicked.connect(self.update_model)
        self.gridLayout_3.addWidget(self.model_list, 8, 1, 1, 1)
        self.locations = QtWidgets.QComboBox(self.widget)
        self.locations.setObjectName("locations")
        self.locations.addItems([' Front', ' Middle', ' Back'])
        font.setPointSize(20)
        self.locations.setFont(font)
        self.gridLayout_3.addWidget(self.locations, 9, 1, 1, 1)
        self.equipment_type_label = QtWidgets.QLabel(self.widget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_type_label.sizePolicy().hasHeightForWidth())
        self.equipment_type_label.setSizePolicy(sizePolicy)
        self.equipment_type_label.setMinimumSize(QtCore.QSize(0, 40))
        self.equipment_type_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.equipment_type_label.setFont(font)
        self.equipment_type_label.setObjectName("equipment_type_label")
        self.gridLayout_3.addWidget(self.equipment_type_label, 5, 0, 1, 1)

        self.equipment_model_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.equipment_model_label.setFont(font)
        self.equipment_model_label.setObjectName("equipment_model_label")
        self.gridLayout_3.addWidget(self.equipment_model_label, 7, 0, 1, 1)

        self.fitting_input_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_input_txt.sizePolicy().hasHeightForWidth())
        self.fitting_input_txt.setSizePolicy(sizePolicy)
        self.fitting_input_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.fitting_input_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.fitting_input_txt.setFont(font)
        self.fitting_input_txt.setObjectName("fitting_input_txt")
        self.gridLayout_3.addWidget(self.fitting_input_txt, 1, 1, 1, 1)

        self.equipment_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_txt.sizePolicy().hasHeightForWidth())
        self.equipment_txt.setSizePolicy(sizePolicy)
        self.equipment_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.equipment_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        self.equipment_txt.setReadOnly(True)
        self.equipment_txt.setObjectName("equipment_txt")
        self.equipment_txt.setFont(font)
        self.gridLayout_3.addWidget(self.equipment_txt, 5, 1, 1, 1)
        self.current_ID_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_ID_label.sizePolicy().hasHeightForWidth())
        self.current_ID_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.current_ID_label.setFont(font)
        self.current_ID_label.setObjectName("current_ID")
        self.gridLayout_3.addWidget(self.current_ID_label, 0, 0, 1, 1)
        self.manufacturer_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_txt.sizePolicy().hasHeightForWidth())
        self.manufacturer_txt.setSizePolicy(sizePolicy)
        self.manufacturer_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.manufacturer_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        self.manufacturer_txt.setReadOnly(True)
        self.manufacturer_txt.setObjectName("manufacturer_txt")
        self.manufacturer_txt.setFont(font)
        self.gridLayout_3.addWidget(self.manufacturer_txt, 3, 1, 1, 1)

        self.manufacturer_list = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_list.sizePolicy().hasHeightForWidth())
        self.manufacturer_list.setSizePolicy(sizePolicy)
        self.manufacturer_list.setObjectName("manufacturer_list")
        self.manufacturer_list.addItems(sorted(self.manufacturers))
        self.manufacturer_list.clicked.connect(self.update_manufacturer)
        self.gridLayout_3.addWidget(self.manufacturer_list, 4, 1, 1, 1)

        self.manufacturer_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.manufacturer_label.setFont(font)
        self.manufacturer_label.setObjectName("manufacturer_label")
        self.gridLayout_3.addWidget(self.manufacturer_label, 3, 0, 1, 1)

        self.equipment_list = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equipment_list.sizePolicy().hasHeightForWidth())
        self.equipment_list.setSizePolicy(sizePolicy)
        self.equipment_list.setObjectName("equipment_list")
        self.equipment_list.clicked.connect(self.update_equipment)
        self.gridLayout_3.addWidget(self.equipment_list, 6, 1, 1, 1)

        self.location_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_input_label.sizePolicy().hasHeightForWidth())
        self.location_input_label.setSizePolicy(sizePolicy)
        self.location_input_label.setMinimumSize(QtCore.QSize(0, 40))
        self.location_input_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.location_input_label.setFont(font)
        self.location_input_label.setObjectName("location_input_label")
        self.gridLayout_3.addWidget(self.location_input_label, 9, 0, 1, 1)

        self.hose_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hose_input_label.sizePolicy().hasHeightForWidth())
        self.hose_input_label.setSizePolicy(sizePolicy)
        self.hose_input_label.setMinimumSize(QtCore.QSize(0, 40))
        self.hose_input_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.hose_input_label.setFont(font)
        self.hose_input_label.setObjectName("hose_input_label")
        self.gridLayout_3.addWidget(self.hose_input_label, 2, 0, 1, 1)
        self.fitting_input_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fitting_input_label.sizePolicy().hasHeightForWidth())
        self.fitting_input_label.setSizePolicy(sizePolicy)
        self.fitting_input_label.setMinimumSize(QtCore.QSize(0, 40))
        self.fitting_input_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.fitting_input_label.setFont(font)
        self.fitting_input_label.setObjectName("fitting_input_label")
        self.gridLayout_3.addWidget(self.fitting_input_label, 1, 0, 1, 1)
        self.hose_input_txt = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hose_input_txt.sizePolicy().hasHeightForWidth())
        self.hose_input_txt.setSizePolicy(sizePolicy)
        self.hose_input_txt.setMinimumSize(QtCore.QSize(0, 40))
        self.hose_input_txt.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.hose_input_txt.setFont(font)
        self.hose_input_txt.setObjectName("hose_input_txt")
        self.gridLayout_3.addWidget(self.hose_input_txt, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.current_ID = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_ID.sizePolicy().hasHeightForWidth())
        self.current_ID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.current_ID.setFont(font)
        self.current_ID.setObjectName("lcdNumber")
        self.current_ID.setStyleSheet('background-color: white')
        self.current_ID.setMinimumSize(QtCore.QSize(0, 40))
        self.current_ID.setText("")
        self.gridLayout_3.addWidget(self.current_ID, 0, 1, 1, 1)
        font.setPointSize(20)


        self.verticalLayout.addWidget(self.widget)
        self.button_frame = QtWidgets.QFrame(self.information_frame)
        self.button_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_button = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setMinimumSize(0, 50)
        self.cancel_button.clicked.connect(self.cancel)
        self.save_button = QtWidgets.QPushButton(self.button_frame)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save)
        self.save_button.setMinimumSize(0, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.save_button.setFont(font)
        self.save_button.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.submit_button = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.submit_button)
        self.submit_button.setEnabled(False)
        self.submit_button.clicked.connect(self.submit)
        self.submit_button.setMinimumSize(0, 50)
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
        self.mouse_pos_label = QtWidgets.QLabel()
        self.statusBar.addWidget(self.mouse_pos_label)
        self.mouse_pos_label.setText("Mouse position")
        MainWindow.setStatusBar(self.statusBar)
        self.records = QtWidgets.QAction(MainWindow)
        self.records.setObjectName("_Storage")
        self.records.triggered.connect(self.open_records)
        self.records.setShortcut(QtCore.Qt.Key_R | QtCore.Qt.CTRL)
        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self._Menu.addAction(self.records)

        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self._Menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.bboxes = []
        self.thread = Default_Thread.VideoThread()
        self.thread.update_info.connect(self.update_info)
        self.thread.change_pixmap_signal.connect(self.Camera_Display.img_drawer.changePixmap)
        self.thread.update_coord.connect(self.update_coord)
        self.thread.start()

        self.label_state = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predictive Maintenance Concept Demo"))
        self.fitting_count_label.setText(_translate("MainWindow", "No. of Fittings Detected:"))
        self.take_image_button.setText(_translate("MainWindow", "Take Image"))
        self.equipment_type_label.setText(_translate("MainWindow", "Equipment Type:"))
        self.equipment_model_label.setText(_translate("MainWindow", "Equipment Model:"))
        self.location_input_label.setText(_translate("MainWindow", "Location:"))
        self.hose_input_label.setText(_translate("MainWindow", "Hose Type:"))
        self.fitting_input_label.setText(_translate("MainWindow", "Fitting Type:"))
        self.label.setText(_translate("MainWindow", "Currently Selected Hose ID:"))
        self.manufacturer_label.setText(_translate("MainWindow", "Manufacturer:"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.Information_Label.setText(_translate("MainWindow", "Information"))
        self.Camera_Feed_Label.setText(_translate("MainWindow", "Camera Feed"))
        self._Menu.setTitle(_translate("MainWindow", "Menu"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.records.setText(_translate("MainWindow", "Open Records"))
        self.records.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionManual.setText(_translate("MainWindow", "How to Use"))

    def update_manufacturer(self, qindex):
        text = self.manufacturer_list.item(qindex.row()).text()
        self.manufacturer_txt.setText(text)
        self.equipment_list.clear()
        self.model_list.clear()
        self.equipment_txt.setText("")
        self.model_txt.setText("")
        self.equipment_list.addItems(sorted(self.assets[text]))

    def update_equipment(self, qindex):
        text = self.equipment_list.item(qindex.row()).text()
        self.model_list.clear()
        self.model_txt.setText("")
        manufacturer = self.manufacturer_txt.text()

        self.equipment_txt.setText(text)
        self.model_list.addItems(sorted(self.assets[manufacturer][text]))

    def update_model(self, qindex):
        self.model_txt.setText(self.model_list.item(qindex.row()).text())

    def update_info(self, val):
        self.fitting_count_lcd.display(val)

    def update_coord(self, bboxes):
        self.bboxes = bboxes

    def take_image(self):
        self.thread.stop()
        time.sleep(0.1)
        self.cancel_button.setEnabled(True)
        self.save_button.setEnabled(True)
        self.submit_button.setEnabled(True)
        self.take_image_button.setEnabled(False)
        self.record = {'Records': {}}
        self.completed_id = []
        self.hour = datetime.datetime.now().hour
        self.minute = datetime.datetime.now().minute
        self.images = {'original': self.Camera_Display.img_drawer.get_original()}
        self.save_dir = "/Users/cheruichang/Documents/GitHub/Yolov5_Detection/GUI/logs/{}_{}".format(datetime.date.today().strftime("%m%d"), datetime.datetime.now().strftime("%H-%M"))
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        else:
            shutil.rmtree(self.save_dir)
            os.mkdir(self.save_dir)
        self.label_state = True

    def cancel(self):
        self.cancel_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.submit_button.setEnabled(False)
        self.take_image_button.setEnabled(True)
        self.fitting_input_txt.setText("")
        self.hose_input_txt.setText("")
        self.manufacturer_txt.setText("")
        self.equipment_txt.setText("")
        self.model_txt.setText("")
        self.equipment_list.clear()
        self.model_list.clear()

        self.current_ID.setText('')
        self.current_ID.setStyleSheet('background-color: white')
        self.thread = Default_Thread.VideoThread()
        self.thread.update_info.connect(self.update_info)
        self.thread.change_pixmap_signal.connect(self.Camera_Display.img_drawer.changePixmap)
        self.thread.update_coord.connect(self.update_coord)
        self.thread.start()

        self.Camera_Display.img_drawer.completed_bboxes = []
        self.Camera_Display.img_drawer.curr_selected = None
        self.Camera_Display.img_drawer.highlighted_img = None
        self.Camera_Display.img_drawer.curr_color = None

        self.label_state = False

    def save(self):
        qm = QtWidgets.QMessageBox()
        temp = QtWidgets.QWidget()
        self.center(temp)

        if self.current_ID.text() != '':
            if self.current_ID.text() not in self.completed_id:
                self.completed_id.append(self.current_ID.text())
                self.record_info()
                self.record_image()
                self.fitting_input_txt.clear()
                self.hose_input_txt.clear()
                self.current_ID.setText("")
                self.current_ID.setStyleSheet("background-color: white")
                self.Camera_Display.img_drawer.change_original()
            else:
                qm = QtWidgets.QMessageBox()
                temp = QtWidgets.QWidget()
                self.center(temp)
                ret = qm.question(temp, 'Confirmation', "Information for this fitting found,"
                                                        "are you sure to replace it?", qm.Yes | qm.No)
                if ret == qm.Yes:
                    self.record_info()
                    self.record_image()
                    self.fitting_input_txt.clear()
                    self.hose_input_txt.clear()
                    self.current_ID.setText("")
                    self.current_ID.setStyleSheet("background-color: white")
                    self.Camera_Display.img_drawer.change_original()
        else:
            qm.information(temp, '', "Fitting not selected, please select a fitting")

    def record_info(self):
        ID = self.current_ID.text()
        fitting_type = self.fitting_input_txt.text()
        hose_type = self.hose_input_txt.text()
        manufacturer = self.manufacturer_txt.text()
        machine_type = self.equipment_txt.text()
        model = self.model_txt.text()
        location = self.locations.currentText()
        self.record['Records'][ID] = {'Fitting': fitting_type,
                                      'Manufacturer': manufacturer,
                                      'Hose': hose_type,
                                      'Equipment Type': machine_type,
                                      'Model Name': model,
                                      'Location': location}

    def record_image(self):
        ID = self.current_ID.text()
        save_img = self.Camera_Display.img_drawer.get_highlighted()
        color = self.Camera_Display.img_drawer.get_curr_bbox_color()
        color = color.split(", ")
        temp = color[0]
        color[0] = int(color[2].split(')')[0])
        color[1] = int(color[1])
        color[2] = int(temp.split('(')[-1])

        cv2.putText(save_img, ID, (0, 0 + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                    2, tuple(color), 2, lineType=cv2.LINE_AA)

        self.images[ID] = save_img

    def submit(self):
        qm = QtWidgets.QMessageBox()
        temp = QtWidgets.QWidget()
        self.center(temp)
        if len(self.completed_id) == len(self.bboxes):
            ret = qm.question(temp, 'Confirmation', "Are you sure to submit all the saved information?", qm.Yes | qm.No)
        else:
            ret = qm.question(temp, 'Confirmation', "Not all fittings are labeled, "
                                                    "are you sure to submit all the saved information?", qm.Yes | qm.No)

        if ret == qm.Yes:
            with open("{}/record_{}_{}.json".format(self.save_dir, datetime.date.today(), datetime.datetime.now().strftime("%H-%M")), 'w') as save_file:
                # for item in self.record:
                #     save_file.write(str(item) + '\n')
                json.dump(self.record, save_file, indent=4)

                images = self.images.keys()
                for image in images:
                    cv2.imwrite(os.path.join(self.save_dir, image + '.jpg'), self.images[image])

            self.cancel()
        else:
            qm.information(temp, '', "Not Submitted")

    def center(self, window):
        qtRectangle = window.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        window.move(qtRectangle.topLeft())

    def open_records(self):
        path = "/Users/cheruichang/Documents/GitHub/Yolov5_Detection/GUI/logs"
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])


class image_drawer(QtWidgets.QLabel):
    def __init__(self, img, window):
        self.box_colors = {
                      0: '(0, 255, 0)',
                      1: '(255, 255, 0)',
                      2: '(0, 255, 255)',
                      3: '(255, 0, 255)',
                      4: '(200, 0, 200)',
                      5: '(0, 200, 200)',
                      6: '(200, 200, 0)',
                      7: '(200, 200, 200)',
                      8: '(0, 170, 170)',
                      9: '(170, 0, 170)',
                      10: '(170, 170, 0)'
                      }
        super(image_drawer, self).__init__()
        self.setMouseTracking(True)
        self.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.pixmap = QtGui.QPixmap(img)
        self.original_img = img
        self.main_window = window
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.display_width = self.size().width()
        self.display_height = self.size().height()
        self.pix_size = self.pixmap.size()
        self.highlighted_img = None
        self.curr_color = None
        self.curr_selected = None
        self.completed_bboxes = []

    def get_highlighted(self):
        return self.highlighted_img

    def get_original(self):
        return self.original_img

    def get_curr_bbox_color(self):
        return self.curr_color

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter(self)
        point = QtCore.QPoint(0, 0)
        scaledPix = self.pixmap.scaled(size, Qt.KeepAspectRatioByExpanding, transformMode=Qt.SmoothTransformation)
        # start painting the label in the middle of the label
        point.setX((size.width() - scaledPix.width())/2)
        point.setY((size.height() - scaledPix.height())/2)
        point.setX(0)
        point.setY(0)
        painter.drawPixmap(point, scaledPix)
        self.pix_size = scaledPix.size()

    def changePixmap(self, img):
        self.original_img = img
        img = self.convert_cv_qt(img)
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()  # repaint() will trigger the paintEvent(self, event)

    def highlight(self, i, bbox):
        img = Image.fromarray(np.uint8(self.original_img)).convert('RGB')
        img_copy = img.copy()
        size = self.original_img.shape[0]
        xmin = int((bbox[0] - bbox[2] / 2) * size)
        ymin = int((bbox[1] - bbox[3] / 2) * size)
        xmax = int((bbox[0] + bbox[2] / 2) * size)
        ymax = int((bbox[1] + bbox[3] / 2) * size)

        img_crop = img.crop((xmin, ymin, xmax, ymax))
        brightner = ImageEnhance.Brightness(img_crop)
        img_crop = brightner.enhance(1)  # Highlight the bbox region
        dimmer = ImageEnhance.Brightness(img_copy)
        img_copy = dimmer.enhance(0.5)
        img_copy.paste(img_crop, (xmin, ymin, xmax, ymax))

        img = np.array(img_copy)
        self.highlighted_img = img
        self.curr_color = self.box_colors[i]
        img = self.convert_cv_qt(img)
        self.pixmap = QtGui.QPixmap(img)
        self.repaint()

    def change_original(self):
        bbox = self.curr_selected[1]
        size = self.original_img.shape[0]
        xc = int(bbox[0] * size)
        yc = int(bbox[1] * size)

        color = self.curr_color.split(", ")
        temp = color[0]
        color[0] = int(color[2].split(')')[0])
        color[1] = int(color[1])
        color[2] = int(temp.split('(')[-1])
        label = str(self.main_window.hour) + str(self.main_window.minute) + str(self.curr_selected[0])
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                              1.5, thickness=2)
        cv2.putText(self.original_img, label, (int((xc - text_width / 2)), int((yc - text_height / 2))), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1, lineType=cv2.LINE_AA)
        self.changePixmap(self.original_img)
        self.completed_bboxes.append(self.curr_selected[0])

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        try:
            rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
            p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.AspectRatioMode.KeepAspectRatio)
            return QtGui.QPixmap.fromImage(p)
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            self.main_window.mouse_pos_label.setText("x: {}, y: {}".format(event.x(), event.y()))
            try:
                within = False
                for i, bbox in enumerate(self.main_window.bboxes):
                    if self.iswithin(event.x(), event.y(), bbox):
                        within = True
                        self.setCursor(Qt.OpenHandCursor)
                    else:
                        if not within:
                            self.setCursor(Qt.ArrowCursor)
            except Exception as e:
                print(e)
        super(image_drawer, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.main_window.label_state:
                try:
                    within = False
                    for i, bbox in enumerate(self.main_window.bboxes):
                        if self.iswithin(event.x(), event.y(), bbox):
                            if i not in self.completed_bboxes:
                                self.main_window.current_ID.setText(str(self.main_window.hour) + str(self.main_window.minute) + str(i))
                                self.setCursor(Qt.ClosedHandCursor)
                                self.main_window.current_ID.setStyleSheet('background-color: rgb{}'.format(self.box_colors[i]))
                                self.highlight(i, bbox)
                                within = True
                                self.curr_selected = (i, bbox)
                        else:
                            if not within:
                                self.setCursor(Qt.ArrowCursor)
                                self.changePixmap(self.original_img)
                                self.main_window.current_ID.setText('')
                                self.curr_selected = None
                    if not within:
                        self.setCursor(Qt.ArrowCursor)
                        self.changePixmap(self.original_img)
                        self.highlighted_img = None
                        self.main_window.current_ID.setText('')
                        self.main_window.current_ID.setStyleSheet('background-color: white')
                        self.curr_selected = None

                except Exception as e:
                    print(e)
        super(image_drawer, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            try:
                within = False
                for i, bbox in enumerate(self.main_window.bboxes):
                    if self.iswithin(event.x(), event.y(), bbox):
                        self.setCursor(Qt.OpenHandCursor)
                        within = True
                    else:
                        if not within:
                            self.setCursor(Qt.ArrowCursor)
            except Exception as e:
                print(e)
            super(image_drawer, self).mouseReleaseEvent(event)

    def iswithin(self, pt1x, pt1y, bbox):
        xmin = int((bbox[0] - bbox[2] / 2) * self.pix_size.width())
        ymin = int((bbox[1] - bbox[3] / 2) * self.pix_size.height())
        xmax = int((bbox[0] + bbox[2] / 2) * self.pix_size.width())
        ymax = int((bbox[1] + bbox[3] / 2) * self.pix_size.height())

        if xmin <= pt1x <= xmax and ymin <= pt1y <= ymax:
            return True
        else:

            return False


class Camera_Display(QtWidgets.QWidget):
    def __init__(self, frame, window):

        super(Camera_Display, self).__init__(frame)
        self.setMinimumSize(QtCore.QSize(320, 320))
        # self.setMouseTracking(True)
        self.setObjectName("Camera_Display")
        self.main_win = window  # This might not be good practice
        layout = QGridLayout()
        self.img_drawer = image_drawer(r"/Users/cheruichang/Desktop/images/IMG47_1_5.jpg", window)
        layout.addWidget(self.img_drawer)
        self.setLayout(layout)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("""
            QPushButton{
                color: #fff;
                border: black;
                background-color: #0078d4
            }QPushButton:hover {
                background-color: #00599d;
            }
            QPushButton:pressed {
                background-color: #00477c;
            }
            QPushButton:disabled {
                background-color: #77b7e9;
            }
            
    """)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
