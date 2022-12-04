#!/usr/bin/python3
"""This script displays all values in the states table of supplied database
where name matches the argument but is safe from MySQL injections"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
