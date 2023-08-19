#!/usr/bin/python3
"""
    The script that lists all states from the database hbtn_0e_0_usa
    starting with capital letter N
"""
import sys
import MySQLdb
if __name__ == '__main__':
    mydb = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    my_data = mycursor.fetchall()

    for row in my_data:
        print(row)

    mycursor.close()
    mydb.close()
