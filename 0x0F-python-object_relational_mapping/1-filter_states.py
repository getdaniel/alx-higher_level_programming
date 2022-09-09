#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa.
"""
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
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
