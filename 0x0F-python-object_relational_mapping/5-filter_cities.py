#!/usr/bin/python3
"""This script lists all cities from the database filtered by
user-provided state name"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s ORDER BY cities.id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
