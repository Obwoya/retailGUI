# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateUnit.ui'
#
# Created: Sat Dec 07 02:57:39 2013
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

class Ui_UpdatePDUMap(object):
    def setupUi(self, UpdatePDUMap):
        UpdatePDUMap.setObjectName(_fromUtf8("UpdatePDUMap"))
        UpdatePDUMap.resize(342, 192)
        self.gridLayoutWidget_2 = QtGui.QWidget(UpdatePDUMap)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 50, 271, 91))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_dev = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_dev.setStyleSheet(_fromUtf8(""))
        self.label_dev.setObjectName(_fromUtf8("label_dev"))
        self.gridLayout.addWidget(self.label_dev, 0, 0, 1, 1)
        self.error_Dev = QtGui.QLabel(self.gridLayoutWidget_2)
        self.error_Dev.setText(_fromUtf8(""))
        self.error_Dev.setObjectName(_fromUtf8("error_Dev"))
        self.gridLayout.addWidget(self.error_Dev, 0, 2, 1, 1)
        self.label_bar = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_bar.setStyleSheet(_fromUtf8(""))
        self.label_bar.setObjectName(_fromUtf8("label_bar"))
        self.gridLayout.addWidget(self.label_bar, 1, 0, 1, 1)
        self.error_Bar = QtGui.QLabel(self.gridLayoutWidget_2)
        self.error_Bar.setText(_fromUtf8(""))
        self.error_Bar.setObjectName(_fromUtf8("error_Bar"))
        self.gridLayout.addWidget(self.error_Bar, 1, 2, 1, 1)
        self.device_barcode = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.device_barcode.setStyleSheet(_fromUtf8(""))
        self.device_barcode.setObjectName(_fromUtf8("device_barcode"))
        self.gridLayout.addWidget(self.device_barcode, 1, 1, 1, 1)
        self.device_id = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.device_id.setStyleSheet(_fromUtf8(""))
        self.device_id.setObjectName(_fromUtf8("device_id"))
        self.gridLayout.addWidget(self.device_id, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)
        self.horizontalLayoutWidget = QtGui.QWidget(UpdatePDUMap)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 140, 162, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.update_pdu = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.update_pdu.setStyleSheet(_fromUtf8(""))
        self.update_pdu.setObjectName(_fromUtf8("update_pdu"))
        self.horizontalLayout_2.addWidget(self.update_pdu)
        self.cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setStyleSheet(_fromUtf8(""))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout_2.addWidget(self.cancel)
        self.label = QtGui.QLabel(UpdatePDUMap)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(UpdatePDUMap)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), UpdatePDUMap.close)
        QtCore.QMetaObject.connectSlotsByName(UpdatePDUMap)

    def retranslateUi(self, UpdatePDUMap):
        UpdatePDUMap.setWindowTitle(_translate("UpdatePDUMap", "Update PDU Map", None))
        self.label_dev.setText(_translate("UpdatePDUMap", "Device ID", None))
        self.label_bar.setText(_translate("UpdatePDUMap", "Barcode", None))
        self.update_pdu.setText(_translate("UpdatePDUMap", "Remap PDU", None))
        self.cancel.setText(_translate("UpdatePDUMap", "Cancel", None))
        self.label.setText(_translate("UpdatePDUMap", "Remap PDU Unit", None))

