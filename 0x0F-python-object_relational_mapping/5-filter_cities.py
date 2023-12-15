#!/usr/bin/python3
"""
connect to the database and fetch data
"""

import MySQLdb
import sys

if __name__ == '__main__':

    mydb = MySQLdb.connect(
            host="localhost", user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

    cur = mydb.cursor()
    cur.execute("SELECT cities.name\
                FROM cities left join states\
                on states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
