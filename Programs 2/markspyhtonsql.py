import mysql.connector as sq
conn=sq.connect('student.db')
cur=conn.cursor()
a='select * from emply'
cur.execute(" " " create table emply(name text,class integer,roll integer" " ")
for i in range(0,5):
    a=input("enter name")
    b=int(input("enter class in digits"))
    c=int(input("enter roll no"))
    cur.execute(" " "INSERT INTO EMPLy VALUES(?,?,?)" " ",(a,b,c,))
conn.close()
#cur.execute(a)
#cur.execute(a)
#print(cur.fetchall())
#conn.close()
