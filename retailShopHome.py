import sys
import connectDb
import getInfo
import getLists
import retrieveRegional
import subprocess
import os
import getpass
import hashlib
from PyQt4 import QtGui, QtCore
from MainWindow import Ui_MainWindow
from addPerishableWidget import AddNewPerishable
from deletePerishableWidget import DeletePerishable
from restockPerishableWidget import RestockPerishable


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialiseAllViews()

        #widgetPressed = self.ui.tabWidget.currentIndex()
        self.ui.viewall_products.clicked.connect(self.viewProducts)
        self.ui.searchbarcode_products.clicked.connect(self.viewProducts)
        self.ui.searchname_products.clicked.connect(self.viewProducts)

        self.ui.viewall_perishable.clicked.connect(self.viewPerishables)
        self.ui.searchbarcode_perishable.clicked.connect(self.viewPerishables)
        self.ui.searchname_perishable.clicked.connect(self.viewPerishables)
        self.ui.add_perishable.clicked.connect(self.addNewPerishable)
        self.ui.remove_perishable.clicked.connect(self.deletePerishable)
        self.ui.update_perishable.clicked.connect(self.updatePerishable)

        self.ui.viewall_tran.clicked.connect(self.viewTran)
        self.ui.searchid_tran.clicked.connect(self.viewTran)
        self.ui.searchdate_tran.clicked.connect(self.viewTran)

        self.ui.viewall_units.clicked.connect(self.viewUnits)
        self.ui.searchbarcode_units.clicked.connect(self.viewUnits)
        self.ui.searchdev_units.clicked.connect(self.viewUnits)

        self.ui.viewall_promo.clicked.connect(self.viewPromo)
        self.ui.searchbarcode_promo.clicked.connect(self.viewPromo)
        self.ui.searchname_promo.clicked.connect(self.viewPromo)
        self.ui.searchpromo_promo.clicked.connect(self.viewPromo)

        self.ui.orderproducts.clicked.connect(self.orderProducts)
        self.ui.updatestock.clicked.connect(self.updateStockAndProduct)

    def initialiseAllViews(self):
        self.viewProducts()
        self.viewPerishables()
        self.viewTran()
        self.viewUnits()
        self.viewPromo()

    def viewProducts(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        flag = 1
        headerProducts = ['Barcode', 'Name', 'Category', 'Manufacturer', 'Price per Unit', 'Stock']
        columnWidth = [75, 250, 125, 125, 100, 75]
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_products.clear()
                self.ui.lineEdit_2_products.clear()
                count, rowProduct = getLists.getProductList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_products.text()):
                self.ui.lineEdit_2_products.clear()
                barcodeSearch = int(self.ui.lineEdit_1_products.text())
                count, rowProduct = getLists.getProductList(1, barcodeSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_products.clear()
                nameSearch = str(self.ui.lineEdit_2_products.text())
                count, rowProduct = getLists.getProductList(2, nameSearch)
            else:
                flag = 0
                self.ui.lineEdit_1_products.clear()
                self.ui.lineEdit_2_products.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            count, rowProduct = getLists.getProductList(0)
        if flag:
            self.arrayToTable(rowProduct, self.ui.tableWidget_products, headerProducts, columnWidth, count, count, 6)

    def viewPerishables(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        headerProducts = ['Barcode', 'Name', 'Category', 'Manufacturer', 'Price per Unit', 'Stock']
        columnWidth = [75, 250, 125, 125, 100, 75]
        if sender is not None:
            senderEvent = sender.text()

            if senderEvent == "View All":
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                count, rowProduct = getLists.getPerishableList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_perishable.text()):
                self.ui.lineEdit_2_perishable.clear()
                barcodeSearch = int(self.ui.lineEdit_1_perishable.text())
                count, rowProduct = getLists.getPerishableList(1, barcodeSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_perishable.clear()
                nameSearch = str(self.ui.lineEdit_2_perishable.text())
                count, rowProduct = getLists.getPerishableList(2, nameSearch)
            elif senderEvent == "Create New":
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                count, rowProduct = getLists.getPerishableList(0)
            elif senderEvent == "Delete":
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                count, rowProduct = getLists.getPerishableList(0)
            elif senderEvent == "Restock":
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                count, rowProduct = getLists.getPerishableList(0)
            else:
                flag = 0
                self.ui.lineEdit_1_perishable.clear()
                self.ui.lineEdit_2_perishable.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            count, rowProduct = getLists.getPerishableList(0)
        if flag:
            self.arrayToTable(rowProduct, self.ui.tableWidget_perishable, headerProducts, columnWidth, count, count, 6)

    def viewTran(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        headerTrans = ['Transaction ID', 'Cashier Unit', 'Date', 'Total Bill']
        headerTransDetail = ['Transaction ID', 'Barcode', 'Promo ID', 'Quantity', 'Type of Transaction']
        columnWidthTrans = [190, 190, 190, 170]
        columnWidthTransDetail = [170, 170, 170, 100, 130]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_tran.clear()
                self.ui.lineEdit_2_tran.clear()
                count, rowTran = getLists.getTranList(0)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)
            elif (senderEvent == "Transaction ID") & isNumber(self.ui.lineEdit_1_tran.text()):
                self.ui.lineEdit_2_tran.clear()
                idSearch = int(self.ui.lineEdit_1_tran.text())
                count, rowTran = getLists.getTranList(1, idSearch)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTransDetail, columnWidthTransDetail, count, count, 5)
            elif senderEvent == "Date":
                self.ui.lineEdit_1_tran.clear()
                dateSearch = str(self.ui.lineEdit_2_tran.text())
                year = dateSearch[:4]
                month = dateSearch[5:7]
                day = dateSearch[8:]
                if isNumber(year) & isNumber(month) & isNumber(day):
                    dateInput = QtCore.QDate(int(year), int(month), int(day))
                    if dateInput:
                        count, rowTran = getLists.getTranList(2, dateSearch)
                        self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)
                    else:
                        self.ui.lineEdit_1_tran.clear()
                        self.ui.lineEdit_2_tran.clear()
                        self.ui.statusBar.clearMessage()
                        QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
                else:
                    self.ui.lineEdit_1_tran.clear()
                    self.ui.lineEdit_2_tran.clear()
                    self.ui.statusBar.clearMessage()
                    QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")              
            else:
                self.ui.lineEdit_1_tran.clear()
                self.ui.lineEdit_2_tran.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            count, rowTran = getLists.getTranList(0)
            self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)

    def viewUnits(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        headerCashier = ['Cashier Unit ID']
        headerPdu = ['PDU ID', 'Barcode Map']
        columnCashier = [800]
        columnPdu = [385, 385]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_units.clear()
                self.ui.lineEdit_2_units.clear()
                countCashier, rowCashier = getLists.getCashierList(0)
                countPdu, rowPDUs = getLists.getPDUList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_units.text()):
                self.ui.lineEdit_2_units.clear()
                barcodeSearch = int(self.ui.lineEdit_1_units.text())
                countCashier, rowCashier = getLists.getCashierList(0)
                countPdu, rowPDUs = getLists.getPDUList(1, barcodeSearch)
            elif (senderEvent == "Device ID") & isNumber(self.ui.lineEdit_2_units.text()):
                self.ui.lineEdit_1_units.clear()
                nameSearch = int(self.ui.lineEdit_2_units.text())
                countCashier, rowCashier = getLists.getCashierList(2, nameSearch)
                countPdu, rowPDUs = getLists.getPDUList(2, nameSearch)
            else:
                flag = 0
                self.ui.lineEdit_1_units.clear()
                self.ui.lineEdit_2_units.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            countCashier, rowCashier = getLists.getCashierList(0)
            countPdu, rowPDUs = getLists.getPDUList(0)
        if flag:
            self.arrayToTable(rowCashier, self.ui.tableWidget_cashier, headerCashier, columnCashier, countCashier, countCashier, 1)
            self.arrayToTable(rowPDUs, self.ui.tableWidget_pdu, headerPdu, columnPdu, countPdu, countPdu, 2)

    def viewPromo(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        sender = self.sender()
        headerPromo = ['Promo ID', 'Barcode', 'Name', 'Unit Price', 'Stock', 'Promotion Bundle Value']
        columnWidth = [80, 90, 250, 100, 100, 150]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "View All":
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                count, rowPromo = getLists.getPromoList(0)
            elif (senderEvent == "Barcode") & isNumber(self.ui.lineEdit_1_promo.text()):
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                barcodeSearch = int(self.ui.lineEdit_1_promo.text())
                count, rowPromo = getLists.getPromoList(1, barcodeSearch)
            elif (senderEvent == "Promo ID") & isNumber(self.ui.lineEdit_2_promo.text()):
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                idSearch = int(self.ui.lineEdit_2_promo.text())
                count, rowPromo = getLists.getPromoList(2, idSearch)
            elif senderEvent == "Name":
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                nameSearch = str(self.ui.lineEdit_3_promo.text())
                count, rowPromo = getLists.getPromoList(3, nameSearch)
            else:
                flag = 0
                self.ui.lineEdit_1_promo.clear()
                self.ui.lineEdit_2_promo.clear()
                self.ui.lineEdit_3_promo.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            count, rowPromo = getLists.getPromoList(0)
        if flag:
            self.arrayToTable(rowPromo, self.ui.tableWidget_promo, headerPromo, columnWidth, count, count, 6)

    def addNewPerishable(self):
        self.child = AddNewPerishable(self)
        self.child.show()

    def deletePerishable(self):
        self.child = DeletePerishable(self)
        self.child.show()

    def updatePerishable(self):
        self.child = RestockPerishable(self)
        self.child.show()


    def updateStockAndProduct(self):
        self.ui.statusBar.showMessage("Checking for Data, please wait...")
    	data = retrieveRegional.downloadFileFromRegional(1, hashlib.md5("helloworld".encode()))
        self.ui.statusBar.clearMessage()
    	if data is None:
    		self.ui.statusBar.showMessage("Failed to download. Check internet connection", 5000)
    	else:
    		retrieveRegional.processJSON(data)
    		self.ui.statusBar.showMessage("Product List was successfully updated and re-stocked", 5000)

    def orderProducts(self):
        self.ui.statusBar.showMessage("Sending Data, please wait...")
    	proc = subprocess.Popen("php senddata.php", shell=True, stdout=subprocess.PIPE)
    	script_response = proc.stdout.read()
        self.ui.statusBar.clearMessage()
    	if "Sent!" in script_response:
            self.ui.statusBar.showMessage("Orders Sent!", 5000)
    	else:
    		self.ui.statusBar.showMessage("Sending Failed. Check internet connection", 5000)

    def arrayToTable(self, array, qtable, headerLabels, columnWidth, noOfRows, noOfRowsOnce, noOfColumns):
        qtable.setColumnCount(noOfColumns)
        qtable.setRowCount(noOfRowsOnce)
        qtable.setHorizontalHeaderLabels(headerLabels)
        for col in range(noOfColumns):
            qtable.setColumnWidth(col, columnWidth[col])
        for row in range(noOfRowsOnce):
            for column in range(noOfColumns):
                if array[row][column] is not None:
                    if type(array[row][column]) is long:
                        if len(str(array[row][column])) == 8: #if it is barcode, not to express in E notation
                            cellContent = array[row][column]
                        else:    
                            cellContent = float(array[row][column])
                    else:
                        cellContent = str(array[row][column])
                    qtable.setItem(row, column, QtGui.QTableWidgetItem(QtCore.QString("%1").arg(cellContent)))
                else:
                    qtable.setItem(row, column, QtGui.QTableWidgetItem(QtCore.QString("NULL")))
        self.ui.statusBar.clearMessage()


app = QtGui.QApplication(sys.argv) 
frame = MainWindow() 
frame.show() 
sys.exit(app.exec_())