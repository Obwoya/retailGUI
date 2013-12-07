import connectDb
from UpdatePerishable import Ui_UpdatePerishable
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class UpdatePerishable(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_UpdatePerishable()
        self.ui.setupUi(self)
        self.initialiseValues()
        self.ui.lineEdit_Barcode.textChanged.connect(self.initialiseValues)
        self.ui.update.clicked.connect(self.updateProduct)
        self.parent = parent

    def initialiseValues(self):
        self.ui.error_Barcode.clear()
        self.ui.lineEdit_Price.clear()
        self.ui.lineEdit_Manu.clear()
        self.ui.lineEdit_Category.clear()
        self.ui.lineEdit_Name.clear()
        barcode = self.ui.lineEdit_Barcode.text()
        if isNumber(barcode) & (len(str(barcode)) == 8):
            conn, cur = connectDb.connectToDatabase()
            checkForExistence = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode= %d ;" % int(barcode)
            cur.execute(checkForExistence)
            count = cur.fetchone()
            count = count[0]
            if count == 1:
                query = "SELECT name, category, manufacturer, cost FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode= %d" % int(barcode)
                cur.execute(query)
                row = cur.fetchone()
                self.ui.lineEdit_Name.setText(row[0])
                if row[1] is not None:
                    self.ui.lineEdit_Category.setText(row[1])
                if row[2] is not None:
                    self.ui.lineEdit_Manu.setText(row[2])
                self.ui.lineEdit_Price.setText(str(row[3]))
            else:
                self.ui.error_Barcode.setText("*no such perishable product")
            connectDb.closeDatabaseConnection(conn, cur)
        else:
            self.ui.error_Barcode.setText("*no such perishable product")



    def updateProduct(self):
        barcode = self.ui.lineEdit_Barcode.text()
        name = str(self.ui.lineEdit_Name.text())
        category = str(self.ui.lineEdit_Category.text())
        manu = str(self.ui.lineEdit_Manu.text())
        price = self.ui.lineEdit_Price.text()

        self.ui.error_Barcode.clear()
        self.ui.error_Price.clear()
        self.ui.error_Name.clear()
        flag = self.validateInput(barcode, name, category, manu, price)

        if flag != 0 & (len(str(barcode)) == 8):
            barcode = int(barcode)
            price = float(price)
            if (price>0) & (barcode>0):
                conn, cur = connectDb.connectToDatabase()
                checkForExistence = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode= %d ;" % barcode
                cur.execute(checkForExistence)
                count = cur.fetchone()
                count = count[0]
                if count == 1:
                    if len(category) == 0:
                        if len(manu) == 0:
                            insertProduct = "UPDATE product SET name='%s', category=NULL, manufacturer=NULL, cost=%.2f WHERE barcode = %d" % (name, price, barcode)
                        else:
                            insertProduct = "UPDATE product SET name='%s', category=NULL, manufacturer='%s', cost=%.2f WHERE barcode = %d" % (name, manu, price, barcode)
                    else:
                        if len(manu) == 0:
                            insertProduct = "UPDATE product SET name='%s', category='%s', manufacturer=NULL, cost=%.2f WHERE barcode = %d" % (name, category, price, barcode)
                        else:
                            insertProduct = "UPDATE product SET name='%s', category='%s', manufacturer='%s', cost=%.2f WHERE barcode = %d" % (name, category, manu, price, barcode)
                    cur.execute(insertProduct)
                    conn.commit()
                    self.parent.viewPerishables()
                    self.close()
                else:
                    self.ui.message.setText("No Perishable Product with the entered barcode found to update")

                connectDb.closeDatabaseConnection(conn, cur)
            else:
                if int(barcode) <= 0:
                    self.ui.lineEdit_Barcode.clear()
                    self.ui.error_Barcode.setText("*incorrect input")
                elif float(price) <= 0:
                    self.ui.lineEdit_Price.clear()
                    self.ui.error_Price.setText("*incorrect input")
        else:
            self.ui.lineEdit_Price.clear()
            self.ui.lineEdit_Manu.clear()
            self.ui.lineEdit_Category.clear()
            self.ui.lineEdit_Name.clear()


    def validateInput(self, barcode, name, category, manu, price):
        flag = 1
        if len(str(barcode)) == 8:
            if isNumber(barcode):
                barcode = int(barcode)
            else:
                flag = 0
                self.ui.error_Barcode.setText("*incorrect input")
        else:
            flag = 0
            self.ui.error_Barcode.setText("*incorrect input")

        if len(str(price)) > 0:
            if isNumber(price):
                price = float(price)
            else:
                flag = 0
                self.ui.error_Price.setText("*incorrect input")
        else:
            flag = 0
            self.ui.error_Price.setText("*required")

        if len(name) == 0:
            flag = 0
            self.ui.error_Name.setText("*required")

        return flag