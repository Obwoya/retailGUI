# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdatePerishable.ui'
#
# Created: Sat Dec 07 04:19:32 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UpdatePerishable(object):
    def setupUi(self, UpdatePerishable):
        UpdatePerishable.setObjectName(_fromUtf8("UpdatePerishable"))
        UpdatePerishable.resize(421, 334)
        self.label_Heading = QtGui.QLabel(UpdatePerishable)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.message = QtGui.QLabel(UpdatePerishable)
        self.message.setGeometry(QtCore.QRect(20, 50, 341, 16))
        self.message.setText(_fromUtf8(""))
        self.message.setObjectName(_fromUtf8("message"))
        self.layoutWidget = QtGui.QWidget(UpdatePerishable)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 341, 201))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Name = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.gridLayout.addWidget(self.lineEdit_Name, 1, 1, 1, 1)
        self.lineEdit_Manu = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Manu.setObjectName(_fromUtf8("lineEdit_Manu"))
        self.gridLayout.addWidget(self.lineEdit_Manu, 3, 1, 1, 1)
        self.label_Name = QtGui.QLabel(self.layoutWidget)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.label_Category = QtGui.QLabel(self.layoutWidget)
        self.label_Category.setObjectName(_fromUtf8("label_Category"))
        self.gridLayout.addWidget(self.label_Category, 2, 0, 1, 1)
        self.label_Manufacturer = QtGui.QLabel(self.layoutWidget)
        self.label_Manufacturer.setObjectName(_fromUtf8("label_Manufacturer"))
        self.gridLayout.addWidget(self.label_Manufacturer, 3, 0, 1, 1)
        self.lineEdit_Price = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Price.setObjectName(_fromUtf8("lineEdit_Price"))
        self.gridLayout.addWidget(self.lineEdit_Price, 4, 1, 1, 1)
        self.label_Price = QtGui.QLabel(self.layoutWidget)
        self.label_Price.setObjectName(_fromUtf8("label_Price"))
        self.gridLayout.addWidget(self.label_Price, 4, 0, 1, 1)
        self.lineEdit_Category = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Category.setObjectName(_fromUtf8("lineEdit_Category"))
        self.gridLayout.addWidget(self.lineEdit_Category, 2, 1, 1, 1)
        self.label_Barcode = QtGui.QLabel(self.layoutWidget)
        self.label_Barcode.setObjectName(_fromUtf8("label_Barcode"))
        self.gridLayout.addWidget(self.label_Barcode, 0, 0, 1, 1)
        self.error_Name = QtGui.QLabel(self.layoutWidget)
        self.error_Name.setText(_fromUtf8(""))
        self.error_Name.setObjectName(_fromUtf8("error_Name"))
        self.gridLayout.addWidget(self.error_Name, 1, 2, 1, 1)
        self.lineEdit_Barcode = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Barcode.setObjectName(_fromUtf8("lineEdit_Barcode"))
        self.gridLayout.addWidget(self.lineEdit_Barcode, 0, 1, 1, 1)
        self.error_Barcode = QtGui.QLabel(self.layoutWidget)
        self.error_Barcode.setText(_fromUtf8(""))
        self.error_Barcode.setObjectName(_fromUtf8("error_Barcode"))
        self.gridLayout.addWidget(self.error_Barcode, 0, 2, 1, 1)
        self.error_Category = QtGui.QLabel(self.layoutWidget)
        self.error_Category.setText(_fromUtf8(""))
        self.error_Category.setObjectName(_fromUtf8("error_Category"))
        self.gridLayout.addWidget(self.error_Category, 2, 2, 1, 1)
        self.error_Manu = QtGui.QLabel(self.layoutWidget)
        self.error_Manu.setText(_fromUtf8(""))
        self.error_Manu.setObjectName(_fromUtf8("error_Manu"))
        self.gridLayout.addWidget(self.error_Manu, 3, 2, 1, 1)
        self.error_Price = QtGui.QLabel(self.layoutWidget)
        self.error_Price.setText(_fromUtf8(""))
        self.error_Price.setObjectName(_fromUtf8("error_Price"))
        self.gridLayout.addWidget(self.error_Price, 4, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.layoutWidget1 = QtGui.QWidget(UpdatePerishable)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 290, 182, 25))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.update = QtGui.QPushButton(self.layoutWidget1)
        self.update.setObjectName(_fromUtf8("update"))
        self.horizontalLayout.addWidget(self.update)
        self.cancel = QtGui.QPushButton(self.layoutWidget1)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(UpdatePerishable)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), UpdatePerishable.close)
        QtCore.QMetaObject.connectSlotsByName(UpdatePerishable)

    def retranslateUi(self, UpdatePerishable):
        UpdatePerishable.setWindowTitle(_translate("UpdatePerishable", "Update Perishable Product", None))
        self.label_Heading.setText(_translate("UpdatePerishable", "Update A Perishable Product", None))
        self.label_Name.setText(_translate("UpdatePerishable", "Name", None))
        self.label_Category.setText(_translate("UpdatePerishable", "Category", None))
        self.label_Manufacturer.setText(_translate("UpdatePerishable", "Manufacturer", None))
        self.label_Price.setText(_translate("UpdatePerishable", "Unit Price", None))
        self.label_Barcode.setText(_translate("UpdatePerishable", "Barcode", None))
        self.update.setText(_translate("UpdatePerishable", "Update", None))
        self.cancel.setText(_translate("UpdatePerishable", "Cancel", None))

