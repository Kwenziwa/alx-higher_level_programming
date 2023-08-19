#!/usr/bin/python3

"""
    The script that lists all cities in a state from the database
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

    my_csql = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    my_cursor.execute(my_csql, (sys.argv[4],))

    my_data = my_cursor.fetchall()

    print(", ".join([city[0] for city in my_data]))

    my_cursor.close()
    my_db.close()

