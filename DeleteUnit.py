# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteUnit.ui'
#
# Created: Sat Dec 07 02:57:48 2013
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

class Ui_DeleteUnit(object):
    def setupUi(self, DeleteUnit):
        DeleteUnit.setObjectName(_fromUtf8("DeleteUnit"))
        DeleteUnit.resize(364, 127)
        self.label_Heading = QtGui.QLabel(DeleteUnit)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.layoutWidget = QtGui.QWidget(DeleteUnit)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 90, 182, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deleteDevice = QtGui.QPushButton(self.layoutWidget)
        self.deleteDevice.setObjectName(_fromUtf8("deleteDevice"))
        self.horizontalLayout.addWidget(self.deleteDevice)
        self.cancel = QtGui.QPushButton(self.layoutWidget)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayoutWidget = QtGui.QWidget(DeleteUnit)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 281, 41))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Device = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Device.setObjectName(_fromUtf8("label_Device"))
        self.gridLayout.addWidget(self.label_Device, 0, 0, 1, 1)
        self.lineEdit_Device = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Device.setObjectName(_fromUtf8("lineEdit_Device"))
        self.gridLayout.addWidget(self.lineEdit_Device, 0, 1, 1, 1)
        self.error_Device = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Device.setText(_fromUtf8(""))
        self.error_Device.setObjectName(_fromUtf8("error_Device"))
        self.gridLayout.addWidget(self.error_Device, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)

        self.retranslateUi(DeleteUnit)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeleteUnit.close)
        QtCore.QMetaObject.connectSlotsByName(DeleteUnit)

    def retranslateUi(self, DeleteUnit):
        DeleteUnit.setWindowTitle(_translate("DeleteUnit", "Delete Unit", None))
        self.label_Heading.setText(_translate("DeleteUnit", "Delete Cashier/Price Display Unit", None))
        self.deleteDevice.setText(_translate("DeleteUnit", "Delete", None))
        self.cancel.setText(_translate("DeleteUnit", "Cancel", None))
        self.label_Device.setText(_translate("DeleteUnit", "Device ID", None))

