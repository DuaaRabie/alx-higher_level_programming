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
    query = "SELECT cities.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        for element in row:
            print(element, end='')
            if row != rows[(len(rows) - 1)]:
                print(", ", end="")
    print()

    cursor.close()
    db.close()
