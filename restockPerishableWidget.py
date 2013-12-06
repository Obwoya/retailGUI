import connectDb
from RestockPerishable import Ui_RestockPerishable
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class RestockPerishable(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_RestockPerishable()
        self.ui.setupUi(self)
        self.ui.restock.clicked.connect(self.restockProduct)
        self.parent = parent

    def restockProduct(self):
        self.ui.error_Barcode.clear()
        self.ui.error_Stock.clear()
        self.ui.error_Expiry.clear()
        barcode = self.ui.lineEdit_Barcode.text()
        stock = self.ui.lineEdit_Stock.text()
        expiry = self.ui.lineEdit_Expiry.text()

        if (len(str(barcode)) > 0) & (len(str(stock)) > 0) & (len(str(expiry)) > 0):
            if isNumber(barcode) & isNumber(stock):
                year = expiry[:4]
                month = expiry[5:7]
                day = expiry[8:]
                if isNumber(year) & isNumber(month) & isNumber(day):
                    dateInput = QtCore.QDate(int(year), int(month), int(day))
                    if dateInput:
                        barcode = int(barcode)
                        stock = int(stock)
                        today = QtCore.QDate.currentDate()
                        if today<dateInput:
                            if stock>0:
                                conn, cur = connectDb.connectToDatabase()
                                checkForExistence = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode = %d ;" % barcode
                                cur.execute(checkForExistence)
                                count = cur.fetchone()
                                count = count[0]
                                if count != 0:
                                    cur.execute("UPDATE product SET stocklevel=stocklevel+%d WHERE barcode = %d" % (stock, barcode))
                                    cur.execute("INSERT INTO batch VALUES(%d, CURDATE(), %d, '%s')" % (barcode, stock, expiry))
                                else:
                                    self.ui.lineEdit_Barcode.clear()
                                    self.ui.lineEdit_Stock.clear()
                                    self.ui.lineEdit_Expiry.clear()
                                    self.ui.error_Barcode.setText("*no such product exists")
                                conn.commit()
                                connectDb.closeDatabaseConnection(conn, cur)
                                self.parent.viewPerishables()
                                self.close()
                            else:
                                self.ui.lineEdit_Stock.clear()
                                self.ui.error_Stock.setText("*incorrect input")
                        else:
                            self.ui.lineEdit_Expiry.clear()
                            self.ui.error_Expiry.setText("*incorrect date")
                    else:
                        self.ui.lineEdit_Expiry.clear()
                        self.ui.error_Expiry.setText("*incorrect input")
                else:
                    self.ui.lineEdit_Expiry.clear()
                    self.ui.error_Expiry.setText("*incorrect input")
            else:
                if not isNumber(stock):
                    self.ui.lineEdit_Stock.clear()
                    self.ui.error_Stock.setText("*incorrect input")
                if not isNumber(barcode):
                    self.ui.lineEdit_Barcode.clear()
                    self.ui.lineEdit_Stock.clear()
                    self.ui.lineEdit_Expiry.clear()
                    self.ui.error_Barcode.setText("*incorrect input")
        else:
            if len(str(barcode)) == 0:
                self.ui.lineEdit_Barcode.clear()
                self.ui.error_Barcode.setText("*required")
            if len(str(stock)) == 0:
                self.ui.lineEdit_Stock.clear()
                self.ui.error_Stock.setText("*required")
            if len(str(expiry)) == 0:
                self.ui.lineEdit_Expiry.clear()
                self.ui.error_Stock.setText("*required")
