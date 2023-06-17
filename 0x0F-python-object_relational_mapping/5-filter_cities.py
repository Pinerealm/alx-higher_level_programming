#!/usr/bin/python3
"""Lists all cities in a user-provided state from the 
database, hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT c.name FROM cities AS c\
             INNER JOIN states AS s ON c.state_id = s.id\
             WHERE s.name = %s ORDER BY c.id"
    cur.execute(query, (argv[4],))
    print(", ".join(row[0] for row in cur.fetchall()))

    cur.close()
    db.close()
