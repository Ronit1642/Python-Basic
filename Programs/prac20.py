import mysql.connector as my
mycon=my.connect(host='localhost',user='root',passwd='system',database='school')
cursor=mycon.cursor()
q='DELETE FROM student WHERE AGE=20'
cursor.execute(q)
mycon.commit()

cursor.execute('Select * from student')
data=cursor.fetchall()

print(data)
