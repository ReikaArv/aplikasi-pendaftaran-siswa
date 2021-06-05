from GUI import ShowData
import sqlite3
conn= sqlite3.connect("E:/data kuliah/semester 4/PBO 2/project/coding/dbbaru.db")

cur=conn.cursor()
cur.execute('SELECT Nama FROM User')
result = cur.fetchall()
for row in result :
    print (row)