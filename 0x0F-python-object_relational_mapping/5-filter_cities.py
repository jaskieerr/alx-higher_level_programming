#!/usr/bin/python3
'''arizona''' 

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

    query = ("""
        SELECT cities.name FROM cities
        INNER JOIN states ON states.id=cities.state_id
        WHERE states.name LIKE BINARY '{}'
        ORDER BY cities.id"""
        .format(sys.argv[4]))

    cr.execute(query)

    for row in cr:
        print(row[0])
