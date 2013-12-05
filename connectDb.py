#!/usr/bin/python
import MySQLdb

def connectToDatabase():
	conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="yatish", passwd="null", db="3002local")
	cur = conn.cursor() 
	return conn, cur

def closeDatabaseConnection(conn, cur):
	cur.close()
	conn.close()