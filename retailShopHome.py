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


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.viewProducts()
        self.viewPerishables()
        self.viewTran()
        self.viewUnits()
        self.viewPromo()

        #widgetPressed = self.ui.tabWidget.currentIndex()
        self.ui.viewall_products.clicked.connect(self.viewProducts)
        self.ui.viewall_perishable.clicked.connect(self.viewPerishables)
        self.ui.viewall_tran.clicked.connect(self.viewTran)
        self.ui.viewall_units.clicked.connect(self.viewUnits)
        self.ui.viewall_promo.clicked.connect(self.viewPromo)

        self.ui.searchbarcode_products.clicked.connect

        self.ui.orderproducts.clicked.connect(self.orderProducts)
        self.ui.updatestock.clicked.connect(self.updateStockAndProduct)

    def viewProducts(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        count, rowProduct = getLists.getProductList()
        self.arrayToTable(rowProduct, self.ui.tableWidget_products, count, count, 6)

    def viewPerishables(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        count, rowProduct = getLists.getPerishableList()
        self.arrayToTable(rowProduct, self.ui.tableWidget_perishable, count, count, 6)

    def viewTran(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        count, rowTran = getLists.getTranList()
        self.arrayToTable(rowTran, self.ui.tableWidget_tran, count, count, 4)

    def viewUnits(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        self.ui.tableWidget_cashier.setHorizontalHeaderLabels(QtCore.QString('Cashier Device Unit'))
    	count, rowCashier = getLists.getCashierList()
        self.arrayToTable(rowCashier, self.ui.tableWidget_cashier, count, count, 1)
        count, rowPDUs = getLists.getPDUList()
        self.arrayToTable(rowPDUs, self.ui.tableWidget_pdu, count, count, 2)

    def viewPromo(self):
        self.ui.statusBar.showMessage("Loading Data, please wait...")
        count, rowPromo = getLists.getPromoList()
        self.arrayToTable(rowPromo, self.ui.tableWidget_promo, count, count, 6)

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

    def arrayToTable(self, array, qtable, noOfRows, noOfRowsOnce, noOfColumns):
        qtable.setColumnCount(noOfColumns)
        qtable.setRowCount(noOfRowsOnce)
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
                    qtable.setItem(row, column, QtGui.QTableWidgetItem())
        self.ui.statusBar.clearMessage()


app = QtGui.QApplication(sys.argv) 
frame = MainWindow() 
frame.show() 
sys.exit(app.exec_())