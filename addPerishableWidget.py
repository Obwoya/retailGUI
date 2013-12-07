import connectDb
from AddNewPerishable import Ui_AddNewPerishable
from PyQt4 import QtGui, QtCore

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class AddNewPerishable(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_AddNewPerishable()
        self.ui.setupUi(self)
        self.ui.create.clicked.connect(self.addProduct)
        self.parent = parent

    def addProduct(self):
    	barcode = self.ui.lineEdit_Barcode.text()
    	name = str(self.ui.lineEdit_Name.text())
    	category = str(self.ui.lineEdit_Category.text())
    	manu = str(self.ui.lineEdit_Manu.text())
    	price = self.ui.lineEdit_Price.text()
    	stock = self.ui.lineEdit_Stock.text()
    	expiry = self.ui.lineEdit_Expiry.text()

    	self.ui.error_Expiry.clear()
    	self.ui.error_Barcode.clear()
    	self.ui.error_Price.clear()
    	self.ui.error_Stock.clear()
    	self.ui.error_Name.clear()
    	flag = self.validateInput(barcode, name, category, manu, price, stock, expiry)

    	if flag != 0 & (len(str(barcode)) == 8):
    		year = expiry[:4]
    		month = expiry[5:7]
    		day = expiry[8:]
    		if isNumber(year) & isNumber(month) & isNumber(day) & (int(barcode)>=10000000) & (float(price)>0) & (int(stock)>0) & (int(barcode)<=99999999):
    			dateInput = QtCore.QDate(int(year), int(month), int(day))
    			if not dateInput:
    				self.ui.lineEdit_Expiry.clear()
    				self.ui.error_Expiry.setText("*incorrect input")
    			else:
    				today = QtCore.QDate.currentDate()
    				if today>dateInput:
    					self.ui.lineEdit_Expiry.clear()
    					self.ui.error_Expiry.setText("*incorrect date")
    				else:
    					barcode = int(barcode)
    					price = float(price)
    					stock = int(stock)
    					conn, cur = connectDb.connectToDatabase()
    					checkForExistence = "SELECT count(*) FROM product WHERE product.barcode = %d ;" % barcode
    					cur.execute(checkForExistence)
    					count = cur.fetchone()
    					count = count[0]
    					if count == 0:
    						if len(category) == 0:
    							if len(manu) == 0:
    								insertProduct = "INSERT INTO product VALUES(%d, '%s', NULL, NULL, %.2f, %d, 1)" % (barcode, name, price, stock)
    							else:
    								insertProduct = "INSERT INTO product VALUES(%d, '%s', NULL, '%s', %.2f, %d, 1)" % (barcode, name, manu, price, stock)
    						else:
    							if len(manu) == 0:
    								insertProduct = "INSERT INTO product VALUES(%d, '%s', '%s', NULL, %.2f, %d, 1)" % (barcode, name, category, price, stock)
    							else:
    								insertProduct = "INSERT INTO product VALUES(%d, '%s', '%s', '%s', %.2f, %d, 1)" % (barcode, name, category, manu, price, stock)
    						cur.execute(insertProduct)
    						insertBatch = "INSERT INTO batch VALUES(%d, CURDATE(), %d, '%s')" % (barcode, stock, expiry)
    						cur.execute(insertBatch)
    					else:
    						self.ui.message.setText("Cannot Add Product since the barcode already exists")

    					conn.commit()
    					connectDb.closeDatabaseConnection(conn, cur)
    					self.parent.viewPerishables()
    					self.close()
        	else:
                    if (int(barcode) > 99999999) | (int(barcode)<10000000):
                        self.ui.lineEdit_Barcode.clear()
                        self.ui.error_Barcode.setText("*incorrect input")
                    elif float(price) <= 0:
                        self.ui.lineEdit_Price.clear()
                        self.ui.error_Price.setText("*incorrect input")
                    elif int(stock) <= 0:
                        self.ui.lineEdit_Stock.clear()
                        self.ui.error_Stock.setText("*incorrect input")
                    else:
            			self.ui.lineEdit_Expiry.clear()
            			self.ui.error_Expiry.setText("*incorrect input")
    	else:
    		self.ui.lineEdit_Barcode.clear()
    		self.ui.lineEdit_Expiry.clear()
    		self.ui.lineEdit_Stock.clear()
    		self.ui.lineEdit_Price.clear()
    		self.ui.lineEdit_Manu.clear()
    		self.ui.lineEdit_Category.clear()
    		self.ui.lineEdit_Name.clear()


    def validateInput(self, barcode, name, category, manu, price, stock, expiry):
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
		
		if len(str(stock)) > 0:
			if isNumber(stock):
				stock = int(stock)
			else:
				flag = 0
				self.ui.error_Stock.setText("*incorrect input")
		else:
			flag = 0
			self.ui.error_Stock.setText("*required")

		if len(name) == 0:
			flag = 0
			self.ui.error_Name.setText("*required")

		if len(expiry) == 0:
			flag = 0
			self.ui.error_Expiry.setText("*required")
		else:
			year = expiry[:4]
			month = expiry[5:7]
			day = expiry[8:]
			if isNumber(year) & isNumber(month) & isNumber(day):
				dateInput = QtCore.QDate(int(year), int(month), int(day))
				if not dateInput:
					flag = 0
					self.ui.error_Expiry.setText("*incorrect input")
				else:
					today = QtCore.QDate.currentDate()
					print today
					print dateInput
					print today<dateInput
					if today>dateInput:
						flag = 0
						self.ui.error_Expiry.setText("*incorrect date")
			else:
				flag = 0
				self.ui.error_Expiry.setText("*incorrect input")
		return flag