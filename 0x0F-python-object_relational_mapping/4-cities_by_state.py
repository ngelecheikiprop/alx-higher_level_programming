#!/usr/bin/python3
"""script that lists all states
from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    """run when function is called"""
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cur = db.cursor()
    cur.execute("""SELECT cities.id,
                cities.name AS city_name,
                states.name AS state_name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
