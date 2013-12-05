#!usr/bin/python
import connectDb
import urllib2
import json
import unicodedata
import sys

def downloadFileFromRegional(shopId, key):
	try:
		response = urllib2.urlopen('http://cg3002-20-z.comp.nus.edu.sg/api/download/%d-%s.json' % (shopId, key.hexdigest()))
		return response
	except:
		return None
	
def processJSON(fileData):
	data = json.load(fileData)
	conn, cur = connectDb.connectToDatabase()
	
	for i in data['product_list']:
		barcode = int(i['barcode'])
		name = str(i['name'])
		category = str(i['category'])
		manufacturer = str(i['manufacturer'])
		costprice = float(i['costprice'])
		deleted = int(i['deleted'])

		name = removeEscapeChars(name)
		category = removeEscapeChars(category)
		manufacturer = removeEscapeChars(manufacturer)
		

		if deleted == 0:
			deleted = 1
		else:
			deleted = 0
		cur.execute("SELECT count(*) FROM product WHERE barcode = %d;" % barcode)
		countProd = cur.fetchone()
		countProd = countProd[0]
		if countProd == 1:
			cur.execute("UPDATE product SET name = \'%s\', category = \'%s\', manufacturer = \'%s\', cost = %.2f, active = %d WHERE barcode = %d;" % (name, category, manufacturer, costprice, deleted, barcode))
		else :
			cur.execute("INSERT INTO product VALUES(%d, \'%s\', \'%s\', \'%s\', %.2f, %d, %d)" % (barcode, name, category, manufacturer, costprice, 0, deleted))

	count = 0
	for i in data['shipment_list']:
		count +=1
	if count>1:
		for i in data['shipment_list']:
			barcode = int(i['barcode'])
			qty = int(i['quantity'])
			cur.execute("SELECT count(*) FROM product WHERE barcode = %d AND active = 1 ;" % barcode)
			countProd = cur.fetchone()
			countProd = countProd[0]
			if countProd == 1:
				insertStock(barcode, qty, cur)
	else:
		barcode = int(data['shipment_list']['barcode'])
		qty = int(data['shipment_list']['quantity'])
		cur.execute("SELECT count(*) FROM product WHERE barcode = %d AND active = 1 ;" % barcode)
		countProd = cur.fetchone()
		countProd = countProd[0]
		if countProd == 1:
			insertStock(barcode, qty, cur)

	conn.commit()
	connectDb.closeDatabaseConnection(conn, cur)
	fileData.close()


# def processJSONShippingList(fileData):
# 	data = json.load(fileData)
# 	conn, cur = connectDb.connectToDatabase()
# 	count = 0
# 	for i in data['shipment_list']:
# 		count +=1
# 	if count>1:
# 		for i in data['shipment_list']:
# 			barcode = int(i['barcode'])
# 			qty = int(i['quantity'])
# 			cur.execute("SELECT count(*) FROM product WHERE barcode = %d AND active = 1 ;" % barcode)
# 			countProd = cur.fetchone()
# 			countProd = countProd[0]
# 			if countProd == 1:
# 				cur.execute("UPDATE product SET stocklevel = stocklevel + %d WHERE barcode = %d;" % (qty, barcode))
# 				cur.execute("SELECT count(*) FROM batch WHERE barcode = %d AND batchdate = CURDATE() ;" % barcode)
# 				countProd = cur.fetchone()
# 				countProd = countProd[0]
# 				if countProd == 0:
# 					cur.execute("INSERT INTO batch VALUES(%d, CURDATE(), %d, NULL);" % (barcode, qty))
# 	else:
# 		barcode = int(data['shipment_list']['barcode'])
# 		qty = int(data['shipment_list']['quantity'])
# 		cur.execute("SELECT count(*) FROM product WHERE barcode = %d AND active = 1 ;" % barcode)
# 		countProd = cur.fetchone()
# 		countProd = countProd[0]
# 		if countProd == 1:
# 			cur.execute("UPDATE product SET stocklevel = stocklevel + %d WHERE barcode = %d;" % (qty, barcode))
# 			cur.execute("SELECT count(*) FROM batch WHERE barcode = %d AND batchdate = CURDATE() ;" % barcode)
# 			countProd = cur.fetchone()
# 			countProd = countProd[0]
# 			if countProd == 0:
# 				cur.execute("INSERT INTO batch VALUES(%d, CURDATE(), %d, NULL);" % (barcode, qty))

# 	conn.commit()
# 	connectDb.closeDatabaseConnection(conn, cur)
# 	fileData.close()


def removeEscapeChars(name):
	name = name.replace("'", "\\'")
	name = name.replace('"', '\\"')
	return name

def insertStock(barcode, qty, cur):
	cur.execute("SELECT count(*) FROM batch WHERE barcode = %d AND batchdate = CURDATE() ;" % barcode)
	countProd = cur.fetchone()
	countProd = countProd[0]
	if countProd == 0:
		cur.execute("INSERT INTO batch VALUES(%d, CURDATE(), %d, NULL);" % (barcode, qty))
		cur.execute("UPDATE product SET stocklevel = stocklevel + %d WHERE barcode = %d;" % (qty, barcode))