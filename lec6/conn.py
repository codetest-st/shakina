import sqlite3
#connect with SQLtite satabase file 
conn=sqlite3.connect("you.db")
#cursor executes SQL commands
#scursor=conn.cursor()
print("database connected  successfully" )
conn.close()
