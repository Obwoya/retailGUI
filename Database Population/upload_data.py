#! usr/bin/python
import sys
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="yatish", passwd="null", db="3002local")
cur = conn.cursor() 

#cur.execute("DROP TABLE flag; DROP TABLE transactiondetails; DROP TABLE pdumap; DROP table transaction; DROP TABLE manager; DROP TABLE cashier; DROP TABLE promotion; DROP TABLE batch; DROP TABLE product;")

filenames = ["products_local.sql", "batch_local.sql", "promotions.sql",  "cashier.sql", "transaction.sql", "transactionDetails.sql"]
for filename in filenames:
	lines = ""
	with open(filename) as f:
	    lines = f.read().splitlines()

	for query in lines:
		cur.execute(query)
	print filename+" done"
	
cur.execute("CREATE VIEW bill AS (SELECT unitsold*cost AS price, t.transactionid AS id FROM transaction t, transactiondetails td, product p WHERE t.transactionid = td.transactionid AND p.barcode = td.barcode GROUP BY t.transactionid) ")
cur.execute("UPDATE transaction SET price = ( SELECT price FROM bill WHERE id = transactionid)")
cur.execute("DROP VIEW bill")
cur.execute("UPDATE transaction t SET t.DATE = DATE_ADD( t.DATE, INTERVAL 70 DAY )")
conn.commit()
cur.close()
conn.close()