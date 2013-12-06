import connectDb
from UpdateUnit import Ui_UpdatePDUMap
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class RemapUnit(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_UpdatePDUMap()
        self.ui.setupUi(self)
        self.ui.update_pdu.clicked.connect(self.updatePdu)
        self.parent = parent

    def updatePdu(self):
        self.ui.error_Dev.clear()
        self.ui.error_Bar.clear()
        did = self.ui.device_id.text()
        barcode = self.ui.device_barcode.text()

        if (len(str(did))>0) & (len(str(barcode))>0):
            if isNumber(did) & isNumber(barcode) & (len(str(barcode)) == 8):
                did = int(did)
                barcode = int(barcode)
                if did<65536:
                    conn, cur = connectDb.connectToDatabase()
                    checkForExistence = "SELECT count(*) FROM pdumap WHERE pdumap.id = %d ;" % did
                    cur.execute(checkForExistence)
                    count = cur.fetchone()
                    count = count[0]
                    checkForExistence = "SELECT count(*) FROM cashier WHERE cashier.id = %d ;" % did
                    cur.execute(checkForExistence)
                    countOther = cur.fetchone()
                    countOther = countOther[0]
                    if (count == 1) & (countOther == 0):
                        checkForExistence1 = "SELECT count(*) FROM product WHERE product.barcode = %d ;" % barcode
                        cur.execute(checkForExistence1)
                        countProd = cur.fetchone()
                        countProd = countProd[0]
                        if countProd == 1:
                            insertQuery = "UPDATE pdumap SET barcode = %d WHERE id = %d" % (barcode, did)
                            cur.execute(insertQuery)
                            conn.commit()
                            self.parent.viewUnits()
                            self.close()
                        else:
                            self.ui.device_barcode.clear()
                            self.ui.error_Bar.setText("*barcode does not exist")
                    else:
                        self.ui.device_id.clear()
                        self.ui.device_barcode.clear()
                        self.ui.error_Dev.setText("*pdu doesn't exist")
                    connectDb.closeDatabaseConnection(conn, cur)
                    self.parent.viewUnits()
                else:
                    self.ui.device_id.clear()
                    self.ui.device_barcode.clear()
                    self.ui.error_Dev.setText("*id must be <65536")
            else:
                if not isNumber(did):
                    self.ui.device_id.clear()
                    self.ui.device_barcode.clear()
                    self.ui.error_Dev.setText("*incorrect input")
                if not isNumber(barcode):
                    self.ui.device_id.clear()
                    self.ui.device_barcode.clear()
                    self.ui.error_Bar.setText("*incorrect input")
                if (len(str(barcode)) != 8):
                    self.ui.device_id.clear()
                    self.ui.device_barcode.clear()
                    self.ui.error_Bar.setText("*incorrect input")
        else:
            if len(str(did)) == 0:
                self.ui.device_id.clear()
                self.ui.device_barcode.clear()
                self.ui.error_Dev.setText("*required")
            if len(str(barcode)) == 0:
                self.ui.device_barcode.clear()
                self.ui.error_Bar.setText("*required")