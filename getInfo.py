#!usr/bin/python
import connectDb

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getPrice(barcode, qty):
	#This function will return 3 values (barcode of unit price, price of the qty products, corresponding promo used)
	#if both returned values are none: product doesn't exist
	#if second value returned is none: insufficient stock

	conn, cur = connectDb.connectToDatabase()

	cur.execute("SELECT count(*) FROM product WHERE barcode = %d;" % barcode)
	products = cur.fetchone()
	products = products[0]

	if products == 0: #if no such product exists
		connectDb.closeDatabaseConnection(conn, cur)
		return None, None, None
	else: #product exists
		cur.execute("SELECT cost, stocklevel FROM product WHERE barcode = %d;" % barcode)
		products = cur.fetchone()
		costPerUnit = products[0]
		stockAvailable = products[1]

		#check if suffficient stock is available
		if qty>stockAvailable:
			connectDb.closeDatabaseConnection(conn, cur)
			return costPerUnit, None, None
		else:
			#check for promo and return qty cost accordingly
			cur.execute("SELECT promoid, type, value FROM promotion WHERE expiry>CURDATE();")

			bestPromo = 0;
			qtyCost = qty*costPerUnit

			for promos in cur.fetchall():
				promos_type = promos[1]
				#Enter all the different type of promotions here
				if promos_type == 0: #bundle type promotion
					promos_value = promos[2]
					if qty>=promos_value: #if criteria for bundle is met
						newqty = 9*qty*costPerUnit/10
						if newqty < qtyCost: #if bundle promotion is the cheaper of the promotions, then store this as new qtyCost
							qtyCost = newqty
							bestPromo = promos[0]
				elif promos_type == 1: #direct discount per unit promotion
					promos_value = promos[2]
					newqty = 9*qty*costPerUnit/10
					if newqty < qtyCost: #if promotion is the cheaper of the promotions, then store this as new qtyCost
						qtyCost = newqty
						bestPromo = promos[0]

			if bestPromo == 0:
				bestPromo = None
			connectDb.closeDatabaseConnection(conn, cur)
			return costPerUnit, qtyCost, bestPromo


def getCashier(cid, pwd):
	conn, cur = connectDb.connectToDatabase()

	if isNumber(cid) == True & isNumber(pwd) == True:
		cid = int(cid)
		pwd = int(pwd)
	else:
		connectDb.closeDatabaseConnection(conn, cur)
		return None

	cur.execute("SELECT count(*) FROM cashier WHERE id=%d AND pwd=%d" % (cid,pwd))
	cashierExist = cur.fetchone()
	if cashierExist[0] == 1:
		connectDb.closeDatabaseConnection(conn, cur)
		return cid
	else :
		connectDb.closeDatabaseConnection(conn, cur)
		return None


def getManager(mid, pwd):
	conn, cur = connectDb.connectToDatabase()
	if isNumber(mid) == True:
		mid = int(mid)
	else:
		connectDb.closeDatabaseConnection(conn, cur)
		return None

	cur.execute("SELECT count(*) FROM manager WHERE id=%d AND pwd=\'%s\'" % (mid,pwd))
	managerExist = cur.fetchone()
	if managerExist[0] == 1:
		connectDb.closeDatabaseConnection(conn, cur)
		return mid
	else :
		connectDb.closeDatabaseConnection(conn, cur)
		return None


def getNextTransactionId():
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT max(transactionid) FROM transaction;")
	maxTrans = cur.fetchone()
	maxTrans = maxTrans[0]
	if maxTrans is None:
		transactionid = 1000000000
	else:
		transactionid = maxTrans+1
	connectDb.closeDatabaseConnection(conn, cur)
	return transactionid

def removeBatch(barcode, batchDate):
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(*) FROM batch WHERE barcode = %d AND batchdate = \'%s\';" % (barcode, batchDate))
	ifbatch = cur.fetchone()
	ifbatch = ifbatch[0]
	if ifbatch == 1:
		cur.execute("SELECT stock FROM batch WHERE barcode = %d AND batchdate = \'%s\';" % (barcode, batchDate))
		stock = cur.fetchone()
		stock = stock[0]
		cur.execute("UPDATE product SET stocklevel = stocklevel - %d WHERE barcode = %d;" % (stock,barcode))
		cur.execute("DELETE FROM batch WHERE barcode = %d AND batchdate = \'%s\';" % (barcode, batchDate))
		tid = getNextTransactionId()
		cur.execute("INSERT INTO transaction values(%d, 1, CURDATE(), 0);" % tid)
		cur.execute("SELECT cost FROM product WHERE barcode = %d;" % barcode)
		cost = cur.fetchone()
		cost = cost[0]
		execute.cur("INSERT INTO transactiondetails VALUES(%d, %d, NULL, %d, 'write off');" % (tid, barcode, stock));
		message = "\nWrite-off successful"
	else:
		message = "\nWrite-off not successful"
	conn.commit()
	connectDb.closeDatabaseConnection(conn, cur)
	return message

def getProductInfo(barcode):
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(*) FROM product WHERE barcode = %d;" % (barcode))
	countProduct = cur.fetchone()
	countProduct = countProduct[0]
	if countProduct == 1:
		cur.execute("SELECT * FROM product WHERE barcode = %d;" % barcode)
		prodDetails = cur.fetchall()
		prodDetails = prodDetails[0]
		name = prodDetails[1]
		category = prodDetails[2]
		manufacturer = prodDetails[3]
		costPerUnit = prodDetails[4]
		stocklevel = prodDetails[5]
		connectDb.closeDatabaseConnection(conn, cur)
		return name, category, manufacturer, costPerUnit, stocklevel
	else:
		connectDb.closeDatabaseConnection(conn, cur)
		return None, None, None, None, None
