#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa.

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                        charset='utf8')
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM `states`")
        rstm = cur.fetchall()
    except MySQLdb.Error:
        try:
            rstm = ("MySQLdb Error")
        except IndexError:
            rstm = ("MySQLdb Error - IndexError")
    for index in rstm:
        print(index)
    cur.close()
    db.close()
