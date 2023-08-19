#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
import sys


def list_states(username, password, db_name):

    # Connect to the MySQL server
    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cursor = db_conn.cursor()
    sql_query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql_query)

    # Fetch all the all_states
    all_states = cursor.fetchall()

    # Display the all_states
    for row in all_states:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
        sys.exit(1)

    user_name = sys.argv[1]
    pword = sys.argv[2]
    db_name = sys.argv[3]

    list_states(user_name, pword, db_name)

