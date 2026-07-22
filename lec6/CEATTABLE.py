import sqlite3
print()
conn=sqlite3.connect("you.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS YOU (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    attendance REAL,
    marks REAL,
    result TEXT
)
""")

conn.commit()
cursor.execute("SELECT*FROM YOU")
rows=cursor.fetchall()
print("table data",rows)
#data insert 
cursor.execute("INSERT INTO YOU(id,name,attendance,marks,result) VALUES(1,'Rohit',98.5,98,Pass)")
conn.close()
print("table created successfully")