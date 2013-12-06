# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeletePerishable.ui'
#
# Created: Fri Dec 06 20:28:24 2013
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

class Ui_DeletePerishable(object):
    def setupUi(self, DeletePerishable):
        DeletePerishable.setObjectName(_fromUtf8("DeletePerishable"))
        DeletePerishable.resize(364, 127)
        self.label_Heading = QtGui.QLabel(DeletePerishable)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.layoutWidget = QtGui.QWidget(DeletePerishable)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 90, 182, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deleteProd = QtGui.QPushButton(self.layoutWidget)
        self.deleteProd.setObjectName(_fromUtf8("deleteProd"))
        self.horizontalLayout.addWidget(self.deleteProd)
        self.cancel = QtGui.QPushButton(self.layoutWidget)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayoutWidget = QtGui.QWidget(DeletePerishable)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 281, 41))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
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
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)

        self.retranslateUi(DeletePerishable)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeletePerishable.close)
        QtCore.QMetaObject.connectSlotsByName(DeletePerishable)

    def retranslateUi(self, DeletePerishable):
        DeletePerishable.setWindowTitle(_translate("DeletePerishable", "Delete Perishable Product", None))
        self.label_Heading.setText(_translate("DeletePerishable", "Delete Perishable Product", None))
        self.deleteProd.setText(_translate("DeletePerishable", "Delete", None))
        self.cancel.setText(_translate("DeletePerishable", "Cancel", None))
        self.label_Barcode.setText(_translate("DeletePerishable", "Barcode", None))

