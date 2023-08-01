#17
import mysql.connector as a
b=a.connect("localhost",user = "root",passwd="system",database="prac")
cursor=b.cursor()
if b.is_connected:
    print("connected successfully")
