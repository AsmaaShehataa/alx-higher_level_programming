#!/usr/bin/python3

"""script that takes in the name of a state as
an argument and lists all cities"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
