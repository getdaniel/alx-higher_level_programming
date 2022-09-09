#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa."""

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
    cur.execute("SELECT `cur`.`id`, `cur`.`name`, `st`.`name` \
                FROM `cities` as `cur` \
                INNER JOIN `states` as `st` \
                ON `cur`.`state_id` = `st`.`id` \
                ORDER BY `cur`.`id`")
    [print(city) for city in cur.fetchall()]
