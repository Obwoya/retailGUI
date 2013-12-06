import connectDb
from AddUnit import Ui_NewUnit
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class NewUnit(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_NewUnit()
        self.ui.setupUi(self)
        self.ui.add_cashier.clicked.connect(self.addCashier)
        self.ui.add_pdu.clicked.connect(self.addPdu)
        self.parent = parent

    def addCashier(self):
        self.ui.error_Id.clear()
        self.ui.error_Pwd.clear()
        cid = self.ui.person_id.text()
        pwd = self.ui.person_password.text()

        if (len(str(cid))>0) & (len(str(pwd))>0):
            if isNumber(cid) & isNumber(pwd) & (len(str(pwd)) <= 6):
                cid = int(cid)
                pwd = int(pwd)
                if cid<65536:
                    conn, cur = connectDb.connectToDatabase()
                    checkForExistence = "SELECT count(*) FROM cashier WHERE id = %d ;" % cid
                    cur.execute(checkForExistence)
                    count = cur.fetchone()
                    count = count[0]
                    checkForExistence = "SELECT count(*) FROM pdumap WHERE id = %d ;" % cid
                    cur.execute(checkForExistence)
                    countOther = cur.fetchone()
                    countOther = countOther[0]
                    if (count == 0) & (countOther == 0):
                        insertQuery = "INSERT INTO cashier VALUES(%d, %d, 1)" % (cid, pwd)
                        cur.execute(insertQuery)
                        conn.commit()
                        self.parent.viewUnits()
                        self.close()
                    else:
                        self.ui.person_id.clear()
                        self.ui.person_password.clear()
                        self.ui.error_Id.setText("*device exists")
                    connectDb.closeDatabaseConnection(conn, cur)
                    self.parent.viewUnits()
                else:
                    self.ui.person_id.clear()
                    self.ui.person_password.clear()
                    self.ui.error_Id.setText("*id must be <65536")
            else:
                if not isNumber(cid):
                    self.ui.person_id.clear()
                    self.ui.person_password.clear()
                    self.ui.error_Id.setText("*incorrect input")
                if not isNumber(pwd) | (len(str(pwd)) > 6):
                    self.ui.person_id.clear()
                    self.ui.person_password.clear()
                    self.ui.error_Pwd.setText("*incorrect input")
        else:
            if len(str(cid)) == 0:
                self.ui.person_id.clear()
                self.ui.person_password.clear()
                self.ui.error_Id.setText("*required")
            if len(str(pwd)) == 0:
                self.ui.person_password.clear()
                self.ui.error_Pwd.setText("*required")

    def addPdu(self):
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
                    if (count == 0) & (countOther == 0):
                        checkForExistence1 = "SELECT count(*) FROM product WHERE product.barcode = %d ;" % barcode
                        cur.execute(checkForExistence1)
                        countProd = cur.fetchone()
                        countProd = countProd[0]
                        if countProd == 1:
                            insertQuery = "INSERT INTO pdumap VALUES(%d, %d)" % (did, barcode)
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
                        self.ui.error_Dev.setText("*device exists")
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