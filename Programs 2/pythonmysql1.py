import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
cur.execute(" " " create table stdo(name text,class text,roll integer)" " ")
cur.execute(" " " insert into stdo values('Ronit','XII',19)" " ")
cur.execute(" " " insert into stdo values('Mohan','XII',5)" " ")
cur.execute(" " " insert into stdo values('Ram','XII',14)" " ")
cur.execute(" " " insert into stdo values('Laxman','XII',7)" " ")
cur.execute(" " " select * from stdo" " ")
print(cur.fetchall())
conn.close()
