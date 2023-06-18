#!/usr/bin/python3
"""lists all cities of a searched state (SQLI safe)
"""

import sys
import MySQLdb


def filter_cities(user, passwd, db, searched):
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=passwd,
            db=db
            )
    cur = db.cursor()
    cur.execute(
            "SELECT name FROM cities \
                    WHERE state_id = \
                    (SELECT id FROM states WHERE name = %s) \
                    ORDER BY id",
            [searched]
            )
    rows = cur.fetchall()
    rows_str = ''
    for row in rows:
        rows_str += str(row)
    cur.close()
    db.close()
    rows_str = rows_str.replace("'", "")
    rows_str = rows_str.replace('(', '')
    rows_str = rows_str.replace(')', '')
    rows_str = rows_str.replace(',', ', ')
    print(rows_str[:len(rows_str) - 2])


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    searched = sys.argv[4]
    filter_cities(user, passwd, db, searched)
