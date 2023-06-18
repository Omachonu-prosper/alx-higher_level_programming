#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def select_cities(username, password, database):
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    cur = db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON states.id = cities.state_id'
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    select_cities(username, password, database)
