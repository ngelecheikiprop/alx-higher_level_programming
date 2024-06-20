#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect("localhost", "root", "", "hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("""USE hbtn_0e_0_usa""")
cur.execute("""SELECT * FROM states""")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
db.close()