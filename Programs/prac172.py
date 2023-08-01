import mysql.connector


conn = mysql.connector.connect(
   user='root', password='system', host='localhost', database='school')


cursor = conn.cursor()


cursor.execute("CREATE TABLE student(Name varchar(30),Branch varchar(300), Roll integer(7),Section varchar(20),Age integer(2));")
q="INSERT INTO student(Name,Branch,Roll,Section,Age) VALUES(%s,%s,%s,%s,%s)"

values=[("Ritam Barik","Information Technology",1706254,"IT-3",21),
        ("Rishi kumar","Information Technology",1706253,"IT-3",21),
        ("Rituraj Saha","Information Technology",1706256,"IT-3",20),
        ("Sk Anirban","Computer Science And Engineering",1706271,"CSE-5",21),
       ("Soumya Das","Computer Science And Engineering",1706273,"CSE-2",21)]

cursor.executemany(q,values)
   
   
conn.commit()



print(cursor.rowcount, "record inserted.")




