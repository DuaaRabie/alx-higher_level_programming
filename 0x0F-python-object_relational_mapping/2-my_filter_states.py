#!/usr/bin/python3
""" Module for states select """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{state}'\
            ORDER BY id ASC"\
            .format(state=sys.argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
