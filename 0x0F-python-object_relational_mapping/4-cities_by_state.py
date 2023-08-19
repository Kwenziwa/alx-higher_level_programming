#!/usr/bin/python3

"""
    The script that lists all cities from the database
"""
import sys
import MySQLdb
if __name__ == '__main__':
    my_db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    my_cursor = my_db.cursor()

    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    my_cursor.execute(sql)

    my_data = my_cursor.fetchall()

    for row in my_data:
        print(row)

    my_cursor.close()
    my_db.close()

