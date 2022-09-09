#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    cur = db.cursor()
    try:
        stmt = "SELECT * FROM `states` ORDER BY `id` ASC"
        cur.execute(stmt)
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
