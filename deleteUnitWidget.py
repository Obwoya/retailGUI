import connectDb
from DeleteUnit import Ui_DeleteUnit
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class DeleteUnit(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_DeleteUnit()
        self.ui.setupUi(self)
        self.ui.deleteDevice.clicked.connect(self.deleteDeviceUnit)
        self.parent = parent

    def deleteDeviceUnit(self):
        self.ui.error_Device.clear()
        device = self.ui.lineEdit_Device.text()

        if (len(str(device)) > 0):
            if (isNumber(device)):
                device = int(device)
                conn, cur = connectDb.connectToDatabase()
                checkForExistence = "SELECT count(*) FROM cashier WHERE id = %d ;" % device
                cur.execute(checkForExistence)
                countCashier = cur.fetchone()
                countCashier = countCashier[0]
                checkForExistence = "SELECT count(*) FROM pdumap WHERE id = %d ;" % device
                cur.execute(checkForExistence)
                countPdu = cur.fetchone()
                countPdu = countPdu[0]
                if (countPdu == 1) | (countCashier == 1):
                    if countCashier == 1:
                        query = "UPDATE cashier SET active = 0 WHERE id = %d;" % device
                    if countPdu == 1:
                        query = "DELETE FROM pdumap WHERE id = %d;" % device
                    cur.execute(query)
                    conn.commit()
                    self.parent.viewUnits()
                    self.close()
                else:
                    self.ui.error_Device.setText("*no such device")   
                connectDb.closeDatabaseConnection(conn, cur) 
            else:
                self.ui.error_Device.setText("*incorrect input")    
        else:
            self.ui.error_Device.setText("*required")