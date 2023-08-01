import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()
#cur.execute(" " "create table stud (name text,roll integer,class  text )" " " )
cur.execute(" " "insert into stud values('rohan',1,'XII')" " ")
cur.execute(" " "insert into stud values('rohit',2,'XII')" " ")


cur.execute(" " " select * from stud " " ")
print(cur.fetchall())


conn.close()
