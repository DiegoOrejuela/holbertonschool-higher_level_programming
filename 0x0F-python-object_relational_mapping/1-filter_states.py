#!/usr/bin/python3
"""
1-filter_states | lists all states with a name starting with N (upper N)

"""
import sys
import MySQLdb

if __name__ == "__main__":
    conexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conexion.close()
