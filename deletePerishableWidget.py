import connectDb
from DeletePerishable import Ui_DeletePerishable
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class DeletePerishable(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_DeletePerishable()
        self.ui.setupUi(self)
        self.ui.deleteProd.clicked.connect(self.deleteProduct)
        self.parent = parent

    def deleteProduct(self):
        self.ui.error_Barcode.clear()
        barcode = self.ui.lineEdit_Barcode.text()
        if len(str(barcode)) > 0:
            if isNumber(barcode):
                barcode = int(barcode)
                conn, cur = connectDb.connectToDatabase()
                checkForExistence = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode = %d ;" % barcode
                cur.execute(checkForExistence)
                count = cur.fetchone()
                count = count[0]
                if count != 0:
                    cur.execute("UPDATE product SET active=0 WHERE barcode = %d" % barcode)
                else:
                    self.ui.error_Barcode.setText("*no such product exists")
                conn.commit()
                connectDb.closeDatabaseConnection(conn, cur)
                self.parent.viewPerishables()
                self.close()
            else:
                self.ui.lineEdit_Barcode.clear()
                self.ui.error_Barcode.setText("*incorrect input")
        else:
            self.ui.error_Barcode.setText("*required")