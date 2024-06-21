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
    state = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = '{}'
                ORDER BY cities.id ASC;
                """.format(state))
    states = cur.fetchall()
    for state in states:
        print(state[0], end="")
        if state is not states[-1]:
            print(", ",end="")
    print()
    cur.close()
    db.close()
