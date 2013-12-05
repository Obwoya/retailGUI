#!usr/bin/python
import connectDb

def getCashierList():
	count = None
	rowCashier = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(*) FROM cashier")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT id FROM cashier")
	rowCashier = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowCashier

def getPDUList():
	count = None
	rowPDUs = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(*) FROM pdumap")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT * FROM pdumap")
	rowPDUs = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowPDUs

def getTranList():
	count = None
	rowTran = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(*) FROM transaction")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT * FROM transaction")
	rowTran = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowTran

def getProductList():
	count = None
	rowProducts = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND ISNULL(batch.expiry)")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND ISNULL(b.expiry)")
	rowProducts = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowProducts

def getPerishableList():
	count = None
	rowProducts = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(distinct product.barcode) FROM product, batch WHERE product.barcode=batch.barcode AND product.active=1 AND NOT ISNULL(batch.expiry)")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT distinct p.barcode, p.name, p.category, p.manufacturer, p.cost, p.stocklevel FROM product p, batch b WHERE p.barcode=b.barcode AND p.active=1 AND NOT ISNULL(b.expiry)")
	rowProducts = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowProducts

def getPromoList():
	count = None
	rowPromo = None
	conn, cur = connectDb.connectToDatabase()
	cur.execute("SELECT count(distinct promotion.promoid) FROM product, promotion WHERE product.barcode=promotion.barcode AND product.active=1 AND (ISNULL(promotion.expiry) OR promotion.expiry>CURDATE())")
	count = cur.fetchone()
	count = count[0]
	cur.execute("SELECT distinct pr.promoid, pr.barcode, p.name, p.cost, p.stocklevel, pr.value FROM product p, promotion pr WHERE p.barcode=pr.barcode AND p.active=1 AND (ISNULL(pr.expiry) OR pr.expiry>CURDATE())")
	rowPromo = cur.fetchall()
	connectDb.closeDatabaseConnection(conn, cur)
	return count, rowPromo