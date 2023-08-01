import mysql.connector as sq
a=sq.connect(host='localhost',user='root',password='system',database='homework')
b=a.cursor()
c="select * from sale"
b.execute(c)
print(b.fetchall())

a.close()
