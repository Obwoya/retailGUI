import connectDb
from CreatePromotion import Ui_CreatePromotion
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class CreatePromotion(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_CreatePromotion()
        self.ui.setupUi(self)
        self.ui.create.clicked.connect(self.createPromo)
        self.parent = parent

    def createPromo(self):
        self.ui.error_Barcode.clear()
        self.ui.error_Value.clear()
        self.ui.error_Expiry.clear()
        barcode = self.ui.lineEdit_Barcode.text()
        value = self.ui.lineEdit_Value.text()
        expiry = self.ui.lineEdit_Expiry.text()

        if (len(str(barcode)) > 0) & (len(str(value)) > 0):
            if (isNumber(barcode)) & (isNumber(value)):
                barcode = int(barcode)
                value = int(value)
                conn, cur = connectDb.connectToDatabase()
                query = "SELECT count(*) FROM product WHERE barcode = %d" % barcode
                cur.execute(query)
                count = cur.fetchone()
                count = count[0]
                if count == 1:
                    cur.execute("SELECT max(promoid) FROM promotion;")
                    maxPromo = cur.fetchone()
                    maxPromo = maxPromo[0]
                    if maxPromo is None:
                        promoid = 1
                    else:
                        promoid = maxPromo+1

                    if (len(str(expiry)) > 0):
                        year = expiry[:4]
                        month = expiry[5:7]
                        day = expiry[8:]
                        if isNumber(year) & isNumber(month) & isNumber(day):
                            dateInput = QtCore.QDate(int(year), int(month), int(day))
                            if not dateInput:
                                self.ui.error_Expiry.setText("*incorrect input")
                                self.ui.lineEdit_Expiry.clear()
                            else:
                                today = QtCore.QDate.currentDate()
                                if today>dateInput:
                                    self.ui.error_Expiry.setText("*incorrect date")
                                    self.ui.lineEdit_Expiry.clear()
                                else:
                                    promoQuery = "INSERT INTO promotion VALUES(%d, %d, 1, %d, '%s', 1)" % (barcode, promoid, value, expiry)
                                    cur.execute(promoQuery)
                                    conn.commit()
                                    connectDb.closeDatabaseConnection(conn, cur)
                                    self.parent.viewPromo()
                                    self.close()
                        else:
                            self.ui.error_Expiry.setText("*incorrect input")
                            self.ui.lineEdit_Expiry.clear()
                    else:
                        promoQuery = "INSERT INTO promotion VALUES(%d, %d, 0, %d, NULL, 1)" % (barcode, promoid, value)
                        cur.execute(promoQuery)
                        conn.commit()
                        connectDb.closeDatabaseConnection(conn, cur)
                        self.parent.viewPromo()
                        self.close()
                else:
                    self.ui.error_Barcode.setText("*no such product")
                    self.ui.lineEdit_Expiry.clear()
                    self.ui.lineEdit_Value.clear()
            else:
                if not isNumber(barcode):
                    self.ui.error_Barcode.setText("*incorrect input")
                    self.ui.lineEdit_Expiry.clear()
                    self.ui.lineEdit_Value.clear()
                if not isNumber(value):
                    self.ui.error_Value.setText("*incorrect input")
                    self.ui.lineEdit_Expiry.clear()
                    self.ui.lineEdit_Value.clear()
        else:
            if len(str(barcode)) == 0:
                self.ui.error_Barcode.setText("*required")
            if len(str(value)) == 0:
                self.ui.error_Value.setText("*required")
