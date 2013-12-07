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
from updatePerishableWidget import UpdatePerishable
from restockPerishableWidget import RestockPerishable
from updateUnitWidget import RemapUnit
from addUnitWidget import NewUnit
from deleteUnitWidget import DeleteUnit
from createPromotionWidget import CreatePromotion
from deletePromotionWidget import DeletePromotion
from writeoffWidget import PerformWriteoff
from performTransactionWidget import PerformTransaction


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
        self.ui.stock_perishable.clicked.connect(self.restockPerishable)
        self.ui.update_perishable.clicked.connect(self.updatePerishable)

        self.ui.viewall_tran.clicked.connect(self.viewTran)
        self.ui.searchid_tran.clicked.connect(self.viewTran)
        self.ui.searchdate_tran.clicked.connect(self.viewTran)
        self.ui.add_tran.clicked.connect(self.performTransaction)

        self.ui.viewall_units.clicked.connect(self.viewUnits)
        self.ui.searchbarcode_units.clicked.connect(self.viewUnits)
        self.ui.searchdev_units.clicked.connect(self.viewUnits)
        self.ui.newunit.clicked.connect(self.addUnits)
        self.ui.updateunit.clicked.connect(self.updateUnits)
        self.ui.removeunit.clicked.connect(self.deleteUnits)

        self.ui.viewall_promo.clicked.connect(self.viewPromo)
        self.ui.searchbarcode_promo.clicked.connect(self.viewPromo)
        self.ui.searchname_promo.clicked.connect(self.viewPromo)
        self.ui.searchpromo_promo.clicked.connect(self.viewPromo)
        self.ui.newpromo.clicked.connect(self.createPromo)
        self.ui.removepromo.clicked.connect(self.deletePromo)

        self.ui.orderproducts.clicked.connect(self.orderProducts)
        self.ui.updatestock.clicked.connect(self.updateStockAndProduct)
        self.ui.writeoff.clicked.connect(self.performWriteoff)

    def initialiseAllViews(self):
        self.dashboard()
        self.viewProducts()
        self.viewPerishables()
        self.viewTran()
        self.viewUnits()
        self.viewPromo()

    def dashboard(self):
        conn, cur = connectDb.connectToDatabase()
        noOfTrans = "SELECT count(distinct t.transactionid) FROM transaction t WHERE t.date = CURDATE()"
        cur.execute(noOfTrans)
        countTransDay = cur.fetchone()
        countTransDay = countTransDay[0]
        if countTransDay != 0:
            moneyTrans = "SELECT sum(price) FROM transaction WHERE transaction.date = CURDATE()"
            cur.execute(moneyTrans)
            totalMoney = cur.fetchone()
            totalMoney = totalMoney[0]
            itemsSold = "SELECT sum(td.unitsold) FROM transaction t, transactiondetails td WHERE t.transactionid = td.transactionid AND t.date = CURDATE()"
            cur.execute(itemsSold)
            totalItemsSold = cur.fetchone()
            totalItemsSold = totalItemsSold[0]
        else:
            totalMoney = 0
            totalItemsSold = 0
        self.ui.noTrans.setText("Number of Transactions Today : %d" % countTransDay)
        self.ui.moneyDay.setText("Total Money Received Today : $%.2f" % totalMoney)
        self.ui.noItems.setText("Number of Items sold Today: %d" % totalItemsSold)
        connectDb.closeDatabaseConnection(conn, cur)

    def getProducts(self, option = 0, value = None):
        if option == 0:
            count, rowProduct = getLists.getProductList(0)
        else:
            count, rowProduct = getLists.getProductList(option, value)
        if option != 1:
            self.ui.lineEdit_1_products.clear()
        if option != 2:
            self.ui.lineEdit_2_products.clear()
        return count, rowProduct

    def getPerish(self, option = 0, value = None):
        if option == 0:
            count, rowProduct = getLists.getPerishableList(0)
        else:
            count, rowProduct = getLists.getPerishableList(option, value)
        if option != 1:
            self.ui.lineEdit_1_perishable.clear()
        if option != 2:
            self.ui.lineEdit_2_perishable.clear()
        return count, rowProduct

    def getTransactions(self, option = 0, value = None):
        if option == 0:
            count, rowTran = getLists.getTranList(0)
        else:
            count, rowTran = getLists.getTranList(option, value)
        if option != 1:
            self.ui.lineEdit_1_tran.clear()
        if option != 2:
            self.ui.lineEdit_2_tran.clear()
        return count, rowTran

    def getUnits(self, option = 0, value = None):
        if option == 0:
            countCashier, rowCashier = getLists.getCashierList(0)
            countPdu, rowPDUs = getLists.getPDUList(0)
        elif option == 1:
            countCashier, rowCashier = getLists.getCashierList(0)
            countPdu, rowPDUs = getLists.getPDUList(1, value)
        elif option == 2:
            countCashier, rowCashier = getLists.getCashierList(2, value)
            countPdu, rowPDUs = getLists.getPDUList(2, value)
        if option != 1:
            self.ui.lineEdit_1_units.clear()
        if option != 2:
            self.ui.lineEdit_2_units.clear()
        return countCashier, rowCashier, countPdu, rowPDUs

    def getPromos(self, option = 0, value = None):
        if option == 0:
            count, rowPromo = getLists.getPromoList(0)
        else:
            count, rowPromo = getLists.getPromoList(option, value)
        if option != 1:
            self.ui.lineEdit_1_promo.clear()
        if option != 2:
            self.ui.lineEdit_2_promo.clear()
        if option != 3:
            self.ui.lineEdit_3_promo.clear()
        return count, rowPromo


    def viewProducts(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.dashboard()
        flag = 1
        headerProducts = ['Barcode', 'Name', 'Category', 'Manufacturer', 'Price per Unit', 'Stock']
        columnWidth = [75, 250, 125, 125, 100, 75]
        sender = self.sender()
        if sender is not None:
            senderEvent = sender.text()
            if (senderEvent == "Refresh") | (senderEvent == "Transaction"):
                count, rowProduct = self.getProducts(0)
            elif (senderEvent == "Filter Barcode") & isNumber(self.ui.lineEdit_1_products.text()):
                barcodeSearch = int(self.ui.lineEdit_1_products.text())
                count, rowProduct = self.getProducts(1, barcodeSearch)
            elif senderEvent == "Filter Name":
                nameSearch = str(self.ui.lineEdit_2_products.text())
                count, rowProduct = self.getProducts(2, nameSearch)
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
        if count == 0:
            self.ui.statusBar.showMessage("No Results Found", 2000)    

    def viewPerishables(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.dashboard()
        sender = self.sender()
        headerProducts = ['Barcode', 'Name', 'Category', 'Manufacturer', 'Price per Unit', 'Stock']
        columnWidth = [75, 250, 125, 125, 100, 75]
        if sender is not None:
            senderEvent = sender.text()

            if senderEvent == "Refresh":
                count, rowProduct = self.getPerish(0)
            elif (senderEvent == "Filter Barcode") & isNumber(self.ui.lineEdit_1_perishable.text()):
                barcodeSearch = int(self.ui.lineEdit_1_perishable.text())
                count, rowProduct = self.getPerish(1, barcodeSearch)
            elif senderEvent == "Filter Name":
                nameSearch = str(self.ui.lineEdit_2_perishable.text())
                count, rowProduct = self.getPerish(2, nameSearch)
            elif senderEvent == "Create New":
                count, rowProduct = self.getPerish(0)
            elif senderEvent == "Delete":
                count, rowProduct = self.getPerish(0)
            elif senderEvent == "Restock":
                count, rowProduct = self.getPerish(0)
            elif senderEvent == "Update":
                count, rowProduct = self.getPerish(0)
            elif senderEvent == "Transaction":
                count, rowProduct = self.getPerish(0)
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
        if count == 0:
            self.ui.statusBar.showMessage("No Results Found", 2000)

    def viewTran(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.dashboard()
        sender = self.sender()
        headerTrans = ['Transaction ID', 'Cashier Unit', 'Date', 'Total Bill']
        headerTransDetail = ['Transaction ID', 'Barcode', 'Promo ID', 'Quantity', 'Type of Transaction']
        columnWidthTrans = [190, 190, 190, 170]
        columnWidthTransDetail = [170, 170, 170, 100, 130]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "Refresh":
                count, rowTran = self.getTransactions(0)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)
            elif (senderEvent == "Filter Transaction ID") & isNumber(self.ui.lineEdit_1_tran.text()):
                idSearch = int(self.ui.lineEdit_1_tran.text())
                count, rowTran = self.getTransactions(1, idSearch)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTransDetail, columnWidthTransDetail, count, count, 5)
            elif senderEvent == "Filter Date":
                self.ui.lineEdit_1_tran.clear()
                dateSearch = str(self.ui.lineEdit_2_tran.text())
                year = dateSearch[:4]
                month = dateSearch[5:7]
                day = dateSearch[8:]
                if isNumber(year) & isNumber(month) & isNumber(day):
                    dateInput = QtCore.QDate(int(year), int(month), int(day))
                    if dateInput:
                        count, rowTran = self.getTransactions(2, dateSearch)
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
            elif senderEvent == "Transaction":
                count, rowTran = self.getTransactions(0)
                self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)            
            else:
                self.ui.lineEdit_1_tran.clear()
                self.ui.lineEdit_2_tran.clear()
                self.ui.statusBar.clearMessage()
                QtGui.QMessageBox.about(self, "Error!", "The value entered was not valid   ")
        else:
            count, rowTran = getLists.getTranList(0)
            self.arrayToTable(rowTran, self.ui.tableWidget_tran, headerTrans, columnWidthTrans, count, count, 4)
        if count == 0:
            self.ui.statusBar.showMessage("No Results Found", 2000)

    def viewUnits(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.dashboard()
        sender = self.sender()
        headerCashier = ['Cashier Unit ID']
        headerPdu = ['PDU ID', 'Port', 'Barcode Map']
        columnCashier = [800]
        columnPdu = [260, 260, 260]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "Refresh":
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
            elif (senderEvent == "Filter Barcode") & isNumber(self.ui.lineEdit_1_units.text()):
                barcodeSearch = int(self.ui.lineEdit_1_units.text())
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(1, barcodeSearch)
            elif (senderEvent == "Filter Device ID") & isNumber(self.ui.lineEdit_2_units.text()):
                nameSearch = int(self.ui.lineEdit_2_units.text())
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(2, nameSearch)
            elif (senderEvent == "Add Cashier"):
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
            elif (senderEvent == "Add PDU"):
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
            elif (senderEvent == "Remap PDU"):
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
            elif (senderEvent == "Delete"):
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
            elif (senderEvent == "Transaction"):
                countCashier, rowCashier, countPdu, rowPDUs = self.getUnits(0)
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
            self.arrayToTable(rowPDUs, self.ui.tableWidget_pdu, headerPdu, columnPdu, countPdu, countPdu, 3)
        if (countCashier == 0) & (countPdu == 0):
            self.ui.statusBar.showMessage("No Results Found", 2000)

    def viewPromo(self):
        flag = 1
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.dashboard()
        sender = self.sender()
        headerPromo = ['Promo ID', 'Barcode', 'Name', 'Unit Price', 'Stock', 'Promotion Bundle Value']
        columnWidth = [80, 90, 250, 100, 100, 150]
        if sender is not None:
            senderEvent = sender.text()
            if senderEvent == "Refresh":
                count, rowPromo = self.getPromos(0)
            elif (senderEvent == "Filter Barcode") & isNumber(self.ui.lineEdit_1_promo.text()):
                barcodeSearch = int(self.ui.lineEdit_1_promo.text())
                count, rowPromo = self.getPromos(1, barcodeSearch)
            elif (senderEvent == "Filter Promo ID") & isNumber(self.ui.lineEdit_2_promo.text()):
                idSearch = int(self.ui.lineEdit_2_promo.text())
                count, rowPromo = self.getPromos(2, idSearch)
            elif senderEvent == "Filter Name":
                nameSearch = str(self.ui.lineEdit_3_promo.text())
                count, rowPromo = self.getPromos(3, nameSearch)
            elif senderEvent == "Create":
                count, rowPromo = self.getPromos(0)
            elif senderEvent == "Delete":
                count, rowPromo = self.getPromos(0)
            elif senderEvent == "Transaction":
                count, rowPromo = self.getPromos(0)
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
        if count == 0:
            self.ui.statusBar.showMessage("No Results Found", 2000)


    def addNewPerishable(self):
        self.child = AddNewPerishable(self)
        self.child.show()

    def deletePerishable(self):
        self.child = DeletePerishable(self)
        self.child.show()

    def restockPerishable(self):
        self.child = RestockPerishable(self)
        self.child.show()

    def updatePerishable(self):
        self.child = UpdatePerishable(self)
        self.child.show()

    def addUnits(self):
        self.child = NewUnit(self)
        self.child.show()

    def updateUnits(self):
        self.child = RemapUnit(self)
        self.child.show()

    def deleteUnits(self):
        self.child = DeleteUnit(self)
        self.child.show()

    def createPromo(self):
        self.child = CreatePromotion(self)
        self.child.show()

    def deletePromo(self):
        self.child = DeletePromotion(self)
        self.child.show()

    def performWriteoff(self):
        self.child = PerformWriteoff(self)
        self.child.show()

    def performTransaction(self):
        self.child = PerformTransaction(self)
        self.child.show()


    def updateStockAndProduct(self):
        self.ui.statusBar.showMessage("Checking for Data, please wait...")
        proc = subprocess.Popen("php decryptData.php", shell=True, stdout=subprocess.PIPE)
        script_response = proc.stdout.read()
        self.ui.statusBar.clearMessage()
    	if "finished" in script_response:
            self.ui.statusBar.showMessage("Product List was successfully updated and re-stocked", 5000)
    	else:
    		self.ui.statusBar.showMessage("Failed to download. Check internet connection", 5000)

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


def managerLogin():
    mid, ok = QtGui.QInputDialog.getText(QtGui.QWidget, 'Manager Login', 'Manager Id:')
    pwd, ok = QtGui.QInputDialog.getText(self, 'Manager Login', 'Password:')
    if ok:
        success = getInfo.getManager(mid,pwd)
        if success is not None:
            app = QtGui.QApplication(sys.argv)
            frame = MainWindow() 
            frame.show() 
            sys.exit(app.exec_())
        else:
            ok = QtGui.QMessageBox.information(self, "Information", "Incorrect id or password!")
            if ok:
                managerLogin()


#managerLogin()

app = QtGui.QApplication(sys.argv)
frame = MainWindow() 
frame.show() 
sys.exit(app.exec_())