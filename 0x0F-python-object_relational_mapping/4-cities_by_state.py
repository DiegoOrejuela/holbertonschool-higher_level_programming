#!/usr/bin/python3
"""
4-cities_by_state |  script that lists all cities from the database
hbtn_0e_4_usa

"""
import sys
import MySQLdb

if __name__ == "__main__":
    pass
    conexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")

    cursor = conexion.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""

    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conexion.close()
