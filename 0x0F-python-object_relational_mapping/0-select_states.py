#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb

if __name__ == "__main__":
    my_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cp = my_db.cursor()
    cp.execute("SELECT * FROM `states`")
    [print(state) for state in cp.fetchall()]
