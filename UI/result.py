# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName("result")
        result.resize(800, 551)
        self.centralwidget = QtWidgets.QWidget(result)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(50, 40, 681, 341))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(112)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.ButtonOut = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonOut.setGeometry(QtCore.QRect(310, 420, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ButtonOut.setFont(font)
        self.ButtonOut.setObjectName("ButtonOut")
        result.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(result)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        result.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(result)
        self.statusbar.setObjectName("statusbar")
        result.setStatusBar(self.statusbar)

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        _translate = QtCore.QCoreApplication.translate
        result.setWindowTitle(_translate("result", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("result", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("result", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("result", "New Row"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("result", "New Row"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("result", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("result", "New Row"))
        self.ButtonOut.setText(_translate("result", "退出"))

