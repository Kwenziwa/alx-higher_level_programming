#!/usr/bin/python3
"""
    The script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb
if __name__ == '__main__':
    my_db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = my_db.cursor()
    my_sql = """ SELECT * FROM states
          WHERE name LIKE BINARY '{}'
          ORDER BY id ASC """.format(sys.argv[4])

    cursor.execute(my_sql)

    my_data = cursor.fetchall()

    for row in my_data:
        print(row)

    cursor.close()
    my_db.close()
