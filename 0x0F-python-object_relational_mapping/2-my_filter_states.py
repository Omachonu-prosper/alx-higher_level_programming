#!/usr/bin/python3
"""lists all states with a name matching the searched term
"""

import sys
import MySQLdb


def my_filter_states(user, passwd, db, searched):
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=passwd,
            db=db
            )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states \
                    WHERE name = '{searched}' \
                    ORDER BY id".format(searched=searched)
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    searched = sys.argv[4]
    my_filter_states(user, passwd, db, searched)
