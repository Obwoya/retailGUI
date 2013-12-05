#!usr/bin/python
import connectDb

def getCashierList(option, valueSearch = None):
	count = None
	rowCashier = None
	conn, cur = connectDb.connectToDatabase()
	if option == 0:
		countQuery = "SELECT count(*) FROM cashier"
		resultQuery = "SELECT id FROM cashier"
	elif option == 2:
		countQuery = "SELECT count(*) FROM cashier WHERE id = %d" % valueSearch
		resultQuery = "SELECT id FROM cashier WHERE id = %d" % valueSearch
	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowCashier = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowCashier



def getPDUList(option, valueSearch = None):
	count = None
	rowPDUs = None
	conn, cur = connectDb.connectToDatabase()
	if option == 0:
		countQuery = "SELECT count(*) FROM pdumap"
		resultQuery = "SELECT * FROM pdumap"
	elif option == 1:
		countQuery = "SELECT count(*) FROM pdumap WHERE barcode = %d" % valueSearch
		resultQuery = "SELECT * FROM pdumap WHERE barcode = %d" % valueSearch
	elif option == 2:
		countQuery = "SELECT count(*) FROM pdumap WHERE id = %d" % valueSearch
		resultQuery = "SELECT * FROM pdumap WHERE id = %d" % valueSearch
	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowPDUs = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowPDUs



def getTranList(option, valueSearch = None):
	count = None
	rowTran = None
	conn, cur = connectDb.connectToDatabase()
	if option == 0:
		countQuery = "SELECT count(*) FROM transaction"
		resultQuery = "SELECT * FROM transaction"
	elif option == 1:
		countQuery = "SELECT count(*) FROM transactiondetails WHERE transactionid = %d" % valueSearch
		resultQuery = "SELECT * FROM transactiondetails WHERE transactionid = %d" % valueSearch
	elif option == 2:
		countQuery = "SELECT count(*) FROM transaction t WHERE t.date = '%s'" % valueSearch
		resultQuery = "SELECT * FROM transaction t WHERE t.date = '%s'" % valueSearch
	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowTran = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowTran



def getProductList(option, valueSearch = None):
	count = None
	rowProducts = None
	conn, cur = connectDb.connectToDatabase()
	
	if option == 0:
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND ISNULL(batch.expiry)"
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND ISNULL(b.expiry)"
	elif option == 1:
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND ISNULL(batch.expiry) AND product.barcode= %d" % valueSearch
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND ISNULL(b.expiry) AND p.barcode= %d" % valueSearch
	elif option == 2:
		valueSearch = '%' + valueSearch + '%'
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND ISNULL(batch.expiry) AND product.name LIKE '%s'" % valueSearch
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND ISNULL(b.expiry) AND p.name LIKE '%s'" % valueSearch
	
	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowProducts = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowProducts



def getPerishableList(option, valueSearch = None):
	count = None
	rowProducts = None
	conn, cur = connectDb.connectToDatabase()

	if option == 0:
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry)"
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND NOT ISNULL(b.expiry)"
	elif option == 1:
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.barcode= %d" % valueSearch
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND NOT ISNULL(b.expiry) AND p.barcode= %d" % valueSearch
	elif option == 2:
		valueSearch = '%' + valueSearch + '%'
		countQuery = "SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry) AND product.name LIKE '%s'" % valueSearch
		resultQuery = "SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND NOT ISNULL(b.expiry) AND p.name LIKE '%s'" % valueSearch

	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowProducts = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowProducts



def getPromoList(option, valueSearch = None):
	count = None
	rowPromo = None
	conn, cur = connectDb.connectToDatabase()

	if option == 0:
		countQuery = "SELECT count(distinct promotion.promoid) FROM product, promotion WHERE product.barcode=promotion.barcode AND product.active=1 AND (ISNULL(promotion.expiry) OR promotion.expiry>CURDATE())"
		resultQuery = "SELECT distinct pr.promoid, pr.barcode, p.name, p.cost, p.stocklevel, pr.value FROM product p, promotion pr WHERE p.barcode=pr.barcode AND p.active=1 AND (ISNULL(pr.expiry) OR pr.expiry>CURDATE())"
	elif option == 1:
		countQuery = "SELECT count(distinct promotion.promoid) FROM product, promotion WHERE product.barcode=promotion.barcode AND product.active=1 AND (ISNULL(promotion.expiry) OR promotion.expiry>CURDATE()) AND product.barcode= %d" % valueSearch
		resultQuery = "SELECT distinct pr.promoid, pr.barcode, p.name, p.cost, p.stocklevel, pr.value FROM product p, promotion pr WHERE p.barcode=pr.barcode AND p.active=1 AND (ISNULL(pr.expiry) OR pr.expiry>CURDATE()) AND p.barcode= %d" % valueSearch
	elif option == 2:
		countQuery = "SELECT count(distinct promotion.promoid) FROM product, promotion WHERE product.barcode=promotion.barcode AND product.active=1 AND (ISNULL(promotion.expiry) OR promotion.expiry>CURDATE()) AND promotion.promoid= %d" % valueSearch
		resultQuery = "SELECT distinct pr.promoid, pr.barcode, p.name, p.cost, p.stocklevel, pr.value FROM product p, promotion pr WHERE p.barcode=pr.barcode AND p.active=1 AND (ISNULL(pr.expiry) OR pr.expiry>CURDATE()) AND pr.promoid= %d" % valueSearch
	elif option == 3:
		valueSearch = '%' + valueSearch + '%'
		countQuery = "SELECT count(distinct promotion.promoid) FROM product, promotion WHERE product.barcode=promotion.barcode AND product.active=1 AND (ISNULL(promotion.expiry) OR promotion.expiry>CURDATE()) AND product.name LIKE '%s'" % valueSearch
		resultQuery = "SELECT distinct pr.promoid, pr.barcode, p.name, p.cost, p.stocklevel, pr.value FROM product p, promotion pr WHERE p.barcode=pr.barcode AND p.active=1 AND (ISNULL(pr.expiry) OR pr.expiry>CURDATE()) AND p.name LIKE '%s'" % valueSearch

	cur.execute(countQuery)
	count = cur.fetchone()
	count = count[0]
	cur.execute(resultQuery)
	rowPromo = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowPromo