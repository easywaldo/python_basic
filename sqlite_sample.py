import sqlite3

conn = sqlite3.connect('sql_sample.db')

cur = conn.cursor()

create_sql = """create table if not exists item(
    id integer primary key autoincrement,
    code text not null,
    name text not null,
    price integer not null
);"""

cur.execute(create_sql)

insert_sql = 'insert into item(code, name, price) values (?, ?, ?);'

cur.execute(insert_sql, ('p01', 'python', 30000))

conn.commit()

conn.close()

