#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa.

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
