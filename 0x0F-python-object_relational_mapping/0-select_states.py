#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
db = MySQLdb.connect(f"localhost", "${sys.argv[1]}", "${sys.argv[2]}", "${sys.argv[3]}")
cur = db.cursor()
cur.execute(f"""USE ${sys.argv[3]}""")
cur.execute("""SELECT * FROM states""")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()