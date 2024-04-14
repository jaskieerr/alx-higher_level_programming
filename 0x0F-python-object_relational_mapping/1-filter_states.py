#!/usr/bin/python3
'''selects all states where name start with'''

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1:]

    db_conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cr = db_conn.cursor()

    cr.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    for row in cr:
        print(row)
