#!/usr/bin/python3
'''arizona '''

import MySQLdb
import sys

if __name__ == "__main__":

    db_conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cr = db_conn.cursor()

    cr.execute("SELECT * FROM `states`
            WHERE BINARY `name` = '{}'"
            .format(sys.argv[4]))

    for row in cr:
        print(row)
