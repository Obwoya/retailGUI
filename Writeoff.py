# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiFiles\Writeoff.ui'
#
# Created: Sat Dec 07 09:28:36 2013
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

class Ui_PerformWriteoff(object):
    def setupUi(self, PerformWriteoff):
        PerformWriteoff.setObjectName(_fromUtf8("PerformWriteoff"))
        PerformWriteoff.resize(387, 219)
        self.label = QtGui.QLabel(PerformWriteoff)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayoutWidget = QtGui.QWidget(PerformWriteoff)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 311, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.error_barcode = QtGui.QLabel(self.gridLayoutWidget)
        self.error_barcode.setText(_fromUtf8(""))
        self.error_barcode.setObjectName(_fromUtf8("error_barcode"))
        self.gridLayout.addWidget(self.error_barcode, 0, 2, 1, 1)
        self.lineEdit_barcode = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_barcode.setObjectName(_fromUtf8("lineEdit_barcode"))
        self.gridLayout.addWidget(self.lineEdit_barcode, 0, 1, 1, 1)
        self.label_barcode = QtGui.QLabel(self.gridLayoutWidget)
        self.label_barcode.setObjectName(_fromUtf8("label_barcode"))
        self.gridLayout.addWidget(self.label_barcode, 0, 0, 1, 1)
        self.label_qty = QtGui.QLabel(self.gridLayoutWidget)
        self.label_qty.setObjectName(_fromUtf8("label_qty"))
        self.gridLayout.addWidget(self.label_qty, 1, 0, 1, 1)
        self.error_qty = QtGui.QLabel(self.gridLayoutWidget)
        self.error_qty.setText(_fromUtf8(""))
        self.error_qty.setObjectName(_fromUtf8("error_qty"))
        self.gridLayout.addWidget(self.error_qty, 1, 2, 1, 1)
        self.lineEdit_qty = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_qty.setObjectName(_fromUtf8("lineEdit_qty"))
        self.gridLayout.addWidget(self.lineEdit_qty, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.horizontalLayoutWidget = QtGui.QWidget(PerformWriteoff)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 150, 160, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nextItem = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.nextItem.setObjectName(_fromUtf8("nextItem"))
        self.horizontalLayout.addWidget(self.nextItem)
        self.writeoff = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.writeoff.setObjectName(_fromUtf8("writeoff"))
        self.horizontalLayout.addWidget(self.writeoff)

        self.retranslateUi(PerformWriteoff)
        QtCore.QMetaObject.connectSlotsByName(PerformWriteoff)

    def retranslateUi(self, PerformWriteoff):
        PerformWriteoff.setWindowTitle(_translate("PerformWriteoff", "Perform Write Off", None))
        self.label.setText(_translate("PerformWriteoff", "Product Writeoff", None))
        self.label_barcode.setText(_translate("PerformWriteoff", "Barcode", None))
        self.label_qty.setText(_translate("PerformWriteoff", "Quantity", None))
        self.nextItem.setText(_translate("PerformWriteoff", "Next Item", None))
        self.writeoff.setText(_translate("PerformWriteoff", "Writeoff", None))

