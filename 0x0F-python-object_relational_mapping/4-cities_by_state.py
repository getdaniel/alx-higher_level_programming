#!/usr/bin/python3
# Lists all cities from the database hbtn_0e_4_usa.
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `cur`.`id`, `cur`.`name`, `st`.`name` \
                FROM `cities` as `cur` \
                INNER JOIN `states` as `st` \
                ON `cur`.`state_id` = `st`.`id` \
                ORDER BY `cur`.`id`")
    [print(city) for city in cur.fetchall()]
