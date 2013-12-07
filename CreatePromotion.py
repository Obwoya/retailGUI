# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreatePromotion.ui'
#
# Created: Sat Dec 07 06:03:50 2013
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

class Ui_CreatePromotion(object):
    def setupUi(self, CreatePromotion):
        CreatePromotion.setObjectName(_fromUtf8("CreatePromotion"))
        CreatePromotion.resize(421, 242)
        self.label_Heading = QtGui.QLabel(CreatePromotion)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.layoutWidget = QtGui.QWidget(CreatePromotion)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 371, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Expiry = QtGui.QLabel(self.layoutWidget)
        self.label_Expiry.setObjectName(_fromUtf8("label_Expiry"))
        self.gridLayout.addWidget(self.label_Expiry, 2, 0, 1, 1)
        self.lineEdit_Expiry = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Expiry.setObjectName(_fromUtf8("lineEdit_Expiry"))
        self.gridLayout.addWidget(self.lineEdit_Expiry, 2, 1, 1, 1)
        self.error_Value = QtGui.QLabel(self.layoutWidget)
        self.error_Value.setText(_fromUtf8(""))
        self.error_Value.setObjectName(_fromUtf8("error_Value"))
        self.gridLayout.addWidget(self.error_Value, 1, 2, 1, 1)
        self.label_Barcode = QtGui.QLabel(self.layoutWidget)
        self.label_Barcode.setObjectName(_fromUtf8("label_Barcode"))
        self.gridLayout.addWidget(self.label_Barcode, 0, 0, 1, 1)
        self.lineEdit_Barcode = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Barcode.setObjectName(_fromUtf8("lineEdit_Barcode"))
        self.gridLayout.addWidget(self.lineEdit_Barcode, 0, 1, 1, 1)
        self.error_Barcode = QtGui.QLabel(self.layoutWidget)
        self.error_Barcode.setText(_fromUtf8(""))
        self.error_Barcode.setObjectName(_fromUtf8("error_Barcode"))
        self.gridLayout.addWidget(self.error_Barcode, 0, 2, 1, 1)
        self.error_Expiry = QtGui.QLabel(self.layoutWidget)
        self.error_Expiry.setText(_fromUtf8(""))
        self.error_Expiry.setObjectName(_fromUtf8("error_Expiry"))
        self.gridLayout.addWidget(self.error_Expiry, 2, 2, 1, 1)
        self.lineEdit_Value = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Value.setObjectName(_fromUtf8("lineEdit_Value"))
        self.gridLayout.addWidget(self.lineEdit_Value, 1, 1, 1, 1)
        self.label_Value = QtGui.QLabel(self.layoutWidget)
        self.label_Value.setObjectName(_fromUtf8("label_Value"))
        self.gridLayout.addWidget(self.label_Value, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 70)
        self.layoutWidget1 = QtGui.QWidget(CreatePromotion)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 200, 182, 25))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.create = QtGui.QPushButton(self.layoutWidget1)
        self.create.setObjectName(_fromUtf8("create"))
        self.horizontalLayout.addWidget(self.create)
        self.cancel = QtGui.QPushButton(self.layoutWidget1)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(CreatePromotion)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), CreatePromotion.close)
        QtCore.QMetaObject.connectSlotsByName(CreatePromotion)

    def retranslateUi(self, CreatePromotion):
        CreatePromotion.setWindowTitle(_translate("CreatePromotion", "Create Promotion", None))
        self.label_Heading.setText(_translate("CreatePromotion", "Create A New Promotion", None))
        self.label_Expiry.setText(_translate("CreatePromotion", "Expiry Date(optional)", None))
        self.label_Barcode.setText(_translate("CreatePromotion", "Barcode", None))
        self.label_Value.setText(_translate("CreatePromotion", "Promotion Bundle Value", None))
        self.create.setText(_translate("CreatePromotion", "Create", None))
        self.cancel.setText(_translate("CreatePromotion", "Cancel", None))

