import connectDb
from DeletePromotion import Ui_DeletePromotion
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class DeletePromotion(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_DeletePromotion()
        self.ui.setupUi(self)
        self.ui.deletePromo.clicked.connect(self.removePromo)
        self.parent = parent

    def removePromo(self):
        self.ui.error_Id.clear()
        promoId = self.ui.lineEdit_Id.text()

        if (len(str(promoId)) > 0):
            if (isNumber(promoId)):
                promoId = int(promoId)
                conn, cur = connectDb.connectToDatabase()
                checkForExistence = "SELECT count(*) FROM promotion WHERE promoid = %d AND active = 1;" % promoId
                cur.execute(checkForExistence)
                count = cur.fetchone()
                count = count[0]
                if (count == 1):
                    query = "UPDATE promotion SET active = 0 WHERE promoid = %d;" % promoId
                    cur.execute(query)
                    conn.commit()
                    self.parent.viewPromo()
                    self.close()
                else:
                    self.ui.error_promoId.setText("*no such promoId")   
                connectDb.closeDatabaseConnection(conn, cur) 
            else:
                self.ui.error_promoId.setText("*incorrect input")    
        else:
            self.ui.error_promoId.setText("*required")