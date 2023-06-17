#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa which match the
argument passed to the script; safe from MySQL injections.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
