# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Information(object):
    def setupUi(self, Information):
        Information.setObjectName("Information")
        Information.resize(960, 841)
        self.centralwidget = QtWidgets.QWidget(Information)
        self.centralwidget.setObjectName("centralwidget")
        self.IButtonYes = QtWidgets.QPushButton(self.centralwidget)
        self.IButtonYes.setGeometry(QtCore.QRect(80, 730, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.IButtonYes.setFont(font)
        self.IButtonYes.setObjectName("IButtonYes")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 241, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineName.setFont(font)
        self.lineName.setObjectName("lineName")
        self.horizontalLayout.addWidget(self.lineName)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 60, 241, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineGender = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineGender.setFont(font)
        self.lineGender.setObjectName("lineGender")
        self.horizontalLayout_2.addWidget(self.lineGender)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 120, 241, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.lineAge = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineAge.setFont(font)
        self.lineAge.setObjectName("lineAge")
        self.horizontalLayout_3.addWidget(self.lineAge)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(520, 0, 241, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.linePhone = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.linePhone.setFont(font)
        self.linePhone.setObjectName("linePhone")
        self.horizontalLayout_4.addWidget(self.linePhone)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(520, 60, 241, 71))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.lineAddress = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineAddress.setFont(font)
        self.lineAddress.setObjectName("lineAddress")
        self.horizontalLayout_5.addWidget(self.lineAddress)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(520, 120, 351, 71))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.lineIdentitynum = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineIdentitynum.setFont(font)
        self.lineIdentitynum.setObjectName("lineIdentitynum")
        self.horizontalLayout_6.addWidget(self.lineIdentitynum)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(50, 180, 241, 71))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineSymptom = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineSymptom.setFont(font)
        self.lineSymptom.setObjectName("lineSymptom")
        self.horizontalLayout_7.addWidget(self.lineSymptom)
        self.IButtonInquire = QtWidgets.QPushButton(self.centralwidget)
        self.IButtonInquire.setGeometry(QtCore.QRect(290, 730, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.IButtonInquire.setFont(font)
        self.IButtonInquire.setObjectName("IButtonInquire")
        self.IButtonOut = QtWidgets.QPushButton(self.centralwidget)
        self.IButtonOut.setGeometry(QtCore.QRect(710, 730, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.IButtonOut.setFont(font)
        self.IButtonOut.setObjectName("IButtonOut")
        self.option = QtWidgets.QTableWidget(self.centralwidget)
        self.option.setGeometry(QtCore.QRect(50, 250, 256, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 238, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 255, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 238, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 255, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(84, 238, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 255, 191))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(113, 170, 84))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 127, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.option.setPalette(palette)
        self.option.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.option.setObjectName("option")
        self.option.setColumnCount(0)
        self.option.setRowCount(0)
        self.option.horizontalHeader().setVisible(False)
        self.option.verticalHeader().setVisible(False)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 440, 841, 289))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineLook = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineLook.setFont(font)
        self.lineLook.setObjectName("lineLook")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineLook)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineListen = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineListen.setFont(font)
        self.lineListen.setObjectName("lineListen")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineListen)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineQuestion = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineQuestion.setFont(font)
        self.lineQuestion.setObjectName("lineQuestion")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineQuestion)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineFeel = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineFeel.setFont(font)
        self.lineFeel.setObjectName("lineFeel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineFeel)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineMenstruation = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineMenstruation.setFont(font)
        self.lineMenstruation.setObjectName("lineMenstruation")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineMenstruation)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineLeucorrhoea = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineLeucorrhoea.setFont(font)
        self.lineLeucorrhoea.setObjectName("lineLeucorrhoea")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineLeucorrhoea)
        self.tablewidgetMainSymptom = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidgetMainSymptom.setGeometry(QtCore.QRect(50, 250, 451, 171))
        self.tablewidgetMainSymptom.setObjectName("tablewidgetMainSymptom")
        self.tablewidgetMainSymptom.setColumnCount(0)
        self.tablewidgetMainSymptom.setRowCount(0)
        self.tablewidgetMainSymptom.horizontalHeader().setVisible(False)
        self.tablewidgetMainSymptom.verticalHeader().setVisible(False)
        self.IButtonYes.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget_7.raise_()
        self.IButtonInquire.raise_()
        self.IButtonOut.raise_()
        self.layoutWidget.raise_()
        self.tablewidgetMainSymptom.raise_()
        self.option.raise_()
        Information.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Information)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 25))
        self.menubar.setObjectName("menubar")
        Information.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Information)
        self.statusbar.setObjectName("statusbar")
        Information.setStatusBar(self.statusbar)

        self.retranslateUi(Information)
        QtCore.QMetaObject.connectSlotsByName(Information)

    def retranslateUi(self, Information):
        _translate = QtCore.QCoreApplication.translate
        Information.setWindowTitle(_translate("Information", "MainWindow"))
        self.IButtonYes.setText(_translate("Information", "确定"))
        self.label.setText(_translate("Information", "名字"))
        self.label_9.setText(_translate("Information", "性别"))
        self.label_10.setText(_translate("Information", "年龄"))
        self.label_11.setText(_translate("Information", "手机"))
        self.label_12.setText(_translate("Information", "住址"))
        self.label_13.setText(_translate("Information", "身份证"))
        self.label_14.setText(_translate("Information", "主诉"))
        self.IButtonInquire.setText(_translate("Information", "查询"))
        self.IButtonOut.setText(_translate("Information", "退出"))
        self.label_8.setText(_translate("Information", "望"))
        self.label_15.setText(_translate("Information", "闻"))
        self.label_16.setText(_translate("Information", "问"))
        self.label_17.setText(_translate("Information", "切"))
        self.label_18.setText(_translate("Information", "经"))
        self.label_19.setText(_translate("Information", "带"))

