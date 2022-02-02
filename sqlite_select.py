import sqlite3

conn = sqlite3.connect('sql_sample.db')

cur = conn.cursor()

select_sql = "select * from item"

cur.execute(select_sql)
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()