#!/usr/bin/python3
"""
5-filtier_cities |  script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

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
    query = """
    SELECT cities.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    WHERE states.name = '{}'
    ORDER BY cities.id ASC""".format(sys.argv[4])

    cursor.execute(query)
    query_rows = cursor.fetchall()
    coma = ""
    for row in query_rows:
        print("{}{}".format(coma, row[0]), end="")
        coma = ", "
    print()
    cursor.close()
    conexion.close()
