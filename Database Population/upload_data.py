#! usr/bin/python
import sys
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="yatish", passwd="null", db="3002local")
cur = conn.cursor() 

filename = sys.argv[1]
with open(filename) as f:
    lines = f.read().splitlines()

for query in lines:
	cur.execute(query)
	
conn.commit()
cur.close()
conn.close()