#!/usr/bin/python3
"""Lists all cities of the state given as argument from hbtn_0e_4_usa.

Safe from SQL injection: the user input is passed as a query parameter.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = BINARY %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))
    print(", ".join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()
