#!/usr/bin/python3
"""
Write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == argv[4]]
