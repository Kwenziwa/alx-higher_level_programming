#!/usr/bin/python3
"""
    The script that takes in arguments and displays all values in the states table of 
    hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from 
    MySQL injections!
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

    my_sql = """SELECT * FROM states
          WHERE name = %s
          ORDER BY id ASC"""

    my_cursor.execute(my_sql, (sys.argv[4],))

    data = my_cursor.fetchall()

    for row in data:
        print(row)

    my_cursor.close()
    my_db.close()
