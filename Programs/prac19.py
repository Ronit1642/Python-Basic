import mysql.connector


conn = mysql.connector.connect(
   user='root', password='system', host='localhost', database='school')


cursor = conn.cursor()

cursor.execute("select * from student where Section='IT-3' and Age=20")
d=cursor.fetchall()
print(d)

