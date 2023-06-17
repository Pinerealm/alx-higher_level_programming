#!/usr/bin/python3
"""Lists all cities from the database, hbtn_0e_4_usa."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT c.id, c.name, s.name FROM cities AS c\
             INNER JOIN states AS s ON c.state_id = s.id\
             ORDER BY c.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
