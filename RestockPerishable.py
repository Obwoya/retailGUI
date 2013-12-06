# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RestockPerishable.ui'
#
# Created: Fri Dec 06 23:02:29 2013
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

class Ui_RestockPerishable(object):
    def setupUi(self, RestockPerishable):
        RestockPerishable.setObjectName(_fromUtf8("RestockPerishable"))
        RestockPerishable.resize(349, 199)
        self.label_Heading = QtGui.QLabel(RestockPerishable)
        self.label_Heading.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.gridLayoutWidget = QtGui.QWidget(RestockPerishable)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 281, 92))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_Stock = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Stock.setObjectName(_fromUtf8("lineEdit_Stock"))
        self.gridLayout.addWidget(self.lineEdit_Stock, 1, 1, 1, 1)
        self.error_Stock = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Stock.setText(_fromUtf8(""))
        self.error_Stock.setObjectName(_fromUtf8("error_Stock"))
        self.gridLayout.addWidget(self.error_Stock, 1, 2, 1, 1)
        self.label_Stock = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Stock.setObjectName(_fromUtf8("label_Stock"))
        self.gridLayout.addWidget(self.label_Stock, 1, 0, 1, 1)
        self.label_Barcode = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Barcode.setObjectName(_fromUtf8("label_Barcode"))
        self.gridLayout.addWidget(self.label_Barcode, 0, 0, 1, 1)
        self.lineEdit_Barcode = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Barcode.setObjectName(_fromUtf8("lineEdit_Barcode"))
        self.gridLayout.addWidget(self.lineEdit_Barcode, 0, 1, 1, 1)
        self.error_Barcode = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Barcode.setText(_fromUtf8(""))
        self.error_Barcode.setObjectName(_fromUtf8("error_Barcode"))
        self.gridLayout.addWidget(self.error_Barcode, 0, 2, 1, 1)
        self.label_Expiry = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Expiry.setObjectName(_fromUtf8("label_Expiry"))
        self.gridLayout.addWidget(self.label_Expiry, 2, 0, 1, 1)
        self.lineEdit_Expiry = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Expiry.setObjectName(_fromUtf8("lineEdit_Expiry"))
        self.gridLayout.addWidget(self.lineEdit_Expiry, 2, 1, 1, 1)
        self.error_Expiry = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Expiry.setText(_fromUtf8(""))
        self.error_Expiry.setObjectName(_fromUtf8("error_Expiry"))
        self.gridLayout.addWidget(self.error_Expiry, 2, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.layoutWidget = QtGui.QWidget(RestockPerishable)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 160, 182, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.restock = QtGui.QPushButton(self.layoutWidget)
        self.restock.setObjectName(_fromUtf8("restock"))
        self.horizontalLayout.addWidget(self.restock)
        self.cancel = QtGui.QPushButton(self.layoutWidget)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(RestockPerishable)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), RestockPerishable.close)
        QtCore.QMetaObject.connectSlotsByName(RestockPerishable)

    def retranslateUi(self, RestockPerishable):
        RestockPerishable.setWindowTitle(_translate("RestockPerishable", "Restock Perishable Product", None))
        self.label_Heading.setText(_translate("RestockPerishable", "Restock Perishable Product", None))
        self.label_Stock.setText(_translate("RestockPerishable", "Stock Added", None))
        self.label_Barcode.setText(_translate("RestockPerishable", "Barcode", None))
        self.label_Expiry.setText(_translate("RestockPerishable", "Expiry Date", None))
        self.lineEdit_Expiry.setPlaceholderText(_translate("RestockPerishable", "yyyy-mm-dd", None))
        self.restock.setText(_translate("RestockPerishable", "Restock", None))
        self.cancel.setText(_translate("RestockPerishable", "Cancel", None))

