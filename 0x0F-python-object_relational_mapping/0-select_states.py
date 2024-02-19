#!/usr/bin/python3
""" Module for states select """
import  MySQLdb
import sys


name, pw, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
db = MySQLdb.connect(host="localhost", port=3306, user=name, passwd=pw, db=db_name)
cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
