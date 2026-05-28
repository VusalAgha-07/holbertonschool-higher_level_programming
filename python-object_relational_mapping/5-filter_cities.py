#!/usr/bin/python3
"""
This script connects to a MySQL database.
It lists all cities of a specific state safely from user input.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))
    query_rows = cursor.fetchall()
    cities_list = [row[0] for row in query_rows]
    print(", ".join(cities_list))
    cursor.close()
    db.close()
