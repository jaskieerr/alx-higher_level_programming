#!/usr/bin/python3
'''selects all states from db'''

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

    cr.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in cr:
        print(row)
