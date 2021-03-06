import connectDb
import getInfo
from Writeoff import Ui_PerformWriteoff
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class PerformWriteoff(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_PerformWriteoff()
        self.ui.setupUi(self)
        self.ui.nextItem.clicked.connect(self.nextProduct)
        self.ui.writeoff.clicked.connect(self.completeWriteoff)
        self.parent = parent
        self.items = {}

    def nextProduct(self):
        self.ui.error_barcode.clear()
        self.ui.error_qty.clear()
        barcode = self.ui.lineEdit_barcode.text()
        qty = self.ui.lineEdit_qty.text()

        if (len(str(barcode)) == 8) & (len(str(qty)) > 0):
            if (isNumber(barcode)) & (isNumber(qty)):
                barcode = int(barcode)
                qty = int(qty)
                if (qty>0):
                    conn, cur = connectDb.connectToDatabase()
                    checkExistence = "SELECT count(*) FROM product WHERE active = 1 AND barcode = %d" % barcode
                    checkQty = "SELECT count(*) FROM product WHERE active = 1 AND barcode = %d AND stocklevel >= %d" % (barcode, qty)
                    cur.execute(checkQty)
                    count = cur.fetchone()
                    count = count[0]
                    if count != 0:
                        self.items[barcode] = qty
                        self.ui.lineEdit_qty.clear()
                        self.ui.lineEdit_barcode.clear()
                    else:
                        cur.execute(checkExistence)
                        count = cur.fetchone()
                        count = count[0]
                        if count != 0:
                            self.ui.lineEdit_qty.clear()
                            self.ui.error_qty.setText("*not enough stock")
                        else:
                            self.ui.lineEdit_qty.clear()
                            self.ui.lineEdit_barcode.clear()
                            self.ui.error_barcode.setText("*no such product")
                    connectDb.closeDatabaseConnection(conn, cur)
                else:
                    self.ui.lineEdit_qty.clear()
                    self.ui.error_qty.setText("*incorrect input")
            else:
                if not isNumber(barcode):
                    self.ui.lineEdit_qty.clear()
                    self.ui.lineEdit_barcode.clear()
                    self.ui.error_barcode.setText("*incorrect input")
                if not isNumber(qty):
                    self.ui.lineEdit_qty.clear()
                    self.ui.error_qty.setText("*incorrect input")
        else:
            if (len(str(qty)) == 0):
                self.ui.error_qty.setText("*required")
            if (len(str(barcode)) == 0):
                self.ui.lineEdit_qty.clear()
                self.ui.error_barcode.setText("*required")
            elif (len(str(barcode)) != 8):
                self.ui.lineEdit_qty.clear()
                self.ui.error_barcode.setText("*incorrect input")

    def completeWriteoff(self):
        self.ui.error_barcode.clear()
        self.ui.error_qty.clear()
        barcode = self.ui.lineEdit_barcode.text()
        qty = self.ui.lineEdit_qty.text()

        if (len(str(barcode)) == 8) & (len(str(qty)) > 0):
            if (isNumber(barcode)) & (isNumber(qty)):
                barcode = int(barcode)
                qty = int(qty)
                if (qty < 0):
                    conn, cur = connectDb.connectToDatabase()
                    checkExistence = "SELECT count(*) FROM product WHERE active = 1 AND barcode = %d" % barcode
                    checkQty = "SELECT count(*) FROM product WHERE active = 1 AND barcode = %d AND stocklevel >= %d" % (barcode, qty)
                    cur.execute(checkQty)
                    count = cur.fetchone()
                    count = count[0]
                    if count != 0:
                        self.items[barcode] = qty

                        tid = getInfo.getNextTransactionId()
                        cid = 0 #Manager
                        cur.execute("INSERT INTO transaction VALUES (%d, %d, CURDATE(), 0.00);" % (tid, cid))
                        keys = self.items.keys()
                        cur1 = conn.cursor()
                        for barcode in keys:
                            qty = self.items.get(barcode)
                            cur.execute("SELECT batchdate, stock FROM batch WHERE barcode = %d;" % barcode)
                            stockAccountedFor = 0
                            for allBatches in cur.fetchall():
                                batchStock = allBatches[1]
                                batchDate = allBatches[0]
                                #Even after adding this batch, we are unable to reach the required stock to be removed
                                if stockAccountedFor+batchStock <= qty:
                                    cur1.execute("DELETE FROM batch WHERE barcode = %d AND batchdate = \'%s\';" % (barcode,batchDate))
                                    stockAccountedFor = stockAccountedFor + batchStock
                                else:
                                    cur1.execute("UPDATE batch SET stock = stock - %d WHERE barcode=%d AND batchdate=\'%s\';" % (qty-stockAccountedFor,barcode,batchDate))                      
                                    stockAccountedFor = qty
                            cur.execute("INSERT INTO transactiondetails VALUES(%d, %d, NULL, %d,'writeoff');" % (tid,barcode,qty))
                            cur.execute("UPDATE product SET stocklevel = stocklevel - %d WHERE barcode=%d;" % (qty,barcode))
                        conn.commit()
                        self.close()

                    else:
                        cur.execute(checkExistence)
                        count = cur.fetchone()
                        count = count[0]
                        if count != 0:
                            self.ui.lineEdit_qty.clear()
                            self.ui.error_qty.setText("*not enough stock")
                        else:
                            self.ui.lineEdit_qty.clear()
                            self.ui.lineEdit_barcode.clear()
                            self.ui.error_barcode.setText("*no such product")
                    connectDb.closeDatabaseConnection(conn, cur)
                else:
                    self.ui.lineEdit_qty.clear()
                    self.ui.error_qty.setText("*incorrect input")
            else:
                if not isNumber(barcode):
                    self.ui.lineEdit_qty.clear()
                    self.ui.lineEdit_barcode.clear()
                    self.ui.error_barcode.setText("*incorrect input")
                if not isNumber(qty):
                    self.ui.lineEdit_qty.clear()
                    self.ui.error_qty.setText("*incorrect input")
        else:
            if (len(str(qty)) == 0):
                self.ui.error_qty.setText("*required")
            if (len(str(barcode)) == 0):
                self.ui.lineEdit_qty.clear()
                self.ui.error_barcode.setText("*required")
            elif (len(str(barcode)) != 8):
                self.ui.lineEdit_qty.clear()
                self.ui.error_barcode.setText("*incorrect input")