# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2_Add.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class add(object):
    def setupUi(self, add):
        add.setObjectName("add")
        add.resize(706, 616)
        self.centralwidget = QtWidgets.QWidget(add)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_tianjia = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tianjia.setGeometry(QtCore.QRect(220, 500, 93, 28))
        self.pushButton_tianjia.setObjectName("pushButton_tianjia")
        self.pushButton_out = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_out.setGeometry(QtCore.QRect(360, 500, 93, 28))
        self.pushButton_out.setObjectName("pushButton_out")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(340, 20, 321, 411))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 4, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 5, 2, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 5, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 6, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 6, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 7, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 8, 2, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 8, 3, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 80, 221, 131))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_bingming = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bingming.setObjectName("lineEdit_bingming")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_bingming)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_yaofang = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_yaofang.setText("")
        self.lineEdit_yaofang.setObjectName("lineEdit_yaofang")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_yaofang)
        add.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 26))
        self.menubar.setObjectName("menubar")
        add.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add)
        self.statusbar.setObjectName("statusbar")
        add.setStatusBar(self.statusbar)

        self.retranslateUi(add)
        QtCore.QMetaObject.connectSlotsByName(add)
        add.setTabOrder(self.lineEdit_id, self.lineEdit_bingming)
        add.setTabOrder(self.lineEdit_bingming, self.lineEdit_yaofang)
        add.setTabOrder(self.lineEdit_yaofang, self.lineEdit_1)
        add.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        add.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        add.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        add.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        add.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        add.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        add.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        add.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        add.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        add.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        add.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        add.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        add.setTabOrder(self.lineEdit_13, self.lineEdit_14)
        add.setTabOrder(self.lineEdit_14, self.lineEdit_15)
        add.setTabOrder(self.lineEdit_15, self.lineEdit_16)
        add.setTabOrder(self.lineEdit_16, self.lineEdit_17)
        add.setTabOrder(self.lineEdit_17, self.lineEdit_18)
        add.setTabOrder(self.lineEdit_18, self.pushButton_tianjia)
        add.setTabOrder(self.pushButton_tianjia, self.pushButton_out)

    def retranslateUi(self, add):
        _translate = QtCore.QCoreApplication.translate
        add.setWindowTitle(_translate("add", "MainWindow"))
        self.pushButton_tianjia.setText(_translate("add", "添加"))
        self.pushButton_out.setText(_translate("add", "取消"))
        self.groupBox.setTitle(_translate("add", "药"))
        self.label_4.setText(_translate("add", "1"))
        self.label_13.setText(_translate("add", "10"))
        self.label_5.setText(_translate("add", "2"))
        self.label_14.setText(_translate("add", "11"))
        self.label_6.setText(_translate("add", "3"))
        self.label_15.setText(_translate("add", "12"))
        self.label_7.setText(_translate("add", "4"))
        self.label_16.setText(_translate("add", "13"))
        self.label_8.setText(_translate("add", "5"))
        self.label_17.setText(_translate("add", "14"))
        self.label_9.setText(_translate("add", "6"))
        self.label_18.setText(_translate("add", "15"))
        self.label_10.setText(_translate("add", "7"))
        self.label_19.setText(_translate("add", "16"))
        self.label_11.setText(_translate("add", "8"))
        self.label_20.setText(_translate("add", "17"))
        self.label_12.setText(_translate("add", "9"))
        self.label_21.setText(_translate("add", "18"))
        self.label.setText(_translate("add", "编号"))
        self.label_2.setText(_translate("add", "病名"))
        self.label_3.setText(_translate("add", "药方名"))




class A(QMainWindow, add):
    def __init__(self):
        super(A, self).__init__()
        self.setupUi(self)

    def open(self):
        self.show()

    def close(self):
        self.hide()