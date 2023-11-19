#!/usr/bin/python3
""" Lists all the cities from the database hbtn_0e_4_usa."""

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
    db_cursor = db.cursor()
    db_cursor.execute("SELECT `db_cursor`.`id`, `db_cursor`.`name`, `st`.`name` \
                FROM `cities` as `db_cursor` \
                INNER JOIN `states` as `st` \
                ON `db_cursor`.`state_id` = `st`.`id` \
                ORDER BY `db_cursor`.`id`")
    [print(city) for city in db_cursor.fetchall()]
