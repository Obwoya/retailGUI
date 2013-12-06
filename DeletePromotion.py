# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeletePromotion.ui'
#
# Created: Sat Dec 07 05:52:58 2013
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

class Ui_DeletePromotion(object):
    def setupUi(self, DeletePromotion):
        DeletePromotion.setObjectName(_fromUtf8("DeletePromotion"))
        DeletePromotion.resize(364, 127)
        self.label_Heading = QtGui.QLabel(DeletePromotion)
        self.label_Heading.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_Heading.setObjectName(_fromUtf8("label_Heading"))
        self.layoutWidget = QtGui.QWidget(DeletePromotion)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 90, 182, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deletePromo = QtGui.QPushButton(self.layoutWidget)
        self.deletePromo.setObjectName(_fromUtf8("deletePromo"))
        self.horizontalLayout.addWidget(self.deletePromo)
        self.cancel = QtGui.QPushButton(self.layoutWidget)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayoutWidget = QtGui.QWidget(DeletePromotion)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 311, 41))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Id = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Id.setObjectName(_fromUtf8("label_Id"))
        self.gridLayout.addWidget(self.label_Id, 0, 0, 1, 1)
        self.lineEdit_Id = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Id.setObjectName(_fromUtf8("lineEdit_Id"))
        self.gridLayout.addWidget(self.lineEdit_Id, 0, 1, 1, 1)
        self.error_Id = QtGui.QLabel(self.gridLayoutWidget)
        self.error_Id.setText(_fromUtf8(""))
        self.error_Id.setObjectName(_fromUtf8("error_Id"))
        self.gridLayout.addWidget(self.error_Id, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setColumnStretch(1, 100)
        self.gridLayout.setColumnStretch(2, 50)

        self.retranslateUi(DeletePromotion)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DeletePromotion.close)
        QtCore.QMetaObject.connectSlotsByName(DeletePromotion)

    def retranslateUi(self, DeletePromotion):
        DeletePromotion.setWindowTitle(_translate("DeletePromotion", "Delete Promotion", None))
        self.label_Heading.setText(_translate("DeletePromotion", "Delete Promotion", None))
        self.deletePromo.setText(_translate("DeletePromotion", "Delete", None))
        self.cancel.setText(_translate("DeletePromotion", "Cancel", None))
        self.label_Id.setText(_translate("DeletePromotion", "Promotion ID", None))

