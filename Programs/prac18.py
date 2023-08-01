import mysql.connector


conn = mysql.connector.connect(
   user='root', password='system', host='localhost', database='school')


cursor = conn.cursor()

cursor.execute('select * from student')
choice=int(input("enter your choice  :-    1. fetchone    2. fetchmany       3. fetchall  "))
if choice ==1:
    data=cursor.fetchone()
    print(data)
if choice ==2:
    Data=cursor.fetchmany()
    print(Data)
if choice ==3:
    D_ata=cursor.fetchall()
    print(D_ata)
