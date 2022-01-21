import sqlite3 as sl

conn = sl.connect('my-test.db')


with conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
        );
    """)

sql = 'INSERT INTO USER (id,name,age) VALUES (?,?,?)'
data = [
    (1,'Replete',34),
    (2,'Suspend',45),
    (3,'Crisps',65)
]

with conn:
    conn.executemany(sql,data)

with conn:
    data = conn.execute("SELECT * FROM USER WHERE age >= 40")
    for row in data:
        print(data)
