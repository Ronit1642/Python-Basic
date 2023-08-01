import mysql.connector as my
con=my.connect(host="localhost",user="root",passwd="system",database="prac")
if con.is_connected():
    print("Connected...",end="\n\n")

else:
    print("Error in Connection")

cur=con.cursor()

q1="CREATE TABLE Student(Name varchar(30),Branch varchar(30), Roll integer(7),Section varchar(20),Age integer(2));"
q2="INSERT INTO Student(Name,Branch,Roll,Section,Age) VALUES({},{},{},{},{})".format('Ritam Barik','Information Technology',1706254,'IT-3',21)
q3="INSERT INTO Student(Name,Branch,Roll,Section,Age) VALUES({},{},{},{},{})".format('Rishi kumar','Information Technology',1706253,'IT-3',21)
q4="INSERT INTO Student(Name,Branch,Roll,Section,Age) VALUES({},{},{},{},{})".format('Rituraj Saha','Information Technology',1706256,'IT-3',20)
q5="INSERT INTO Student(Name,Branch,Roll,Section,Age) VALUES({},{},{},{},{})".format('Sk Anirban','Computer Science And Engineering',1706271,'CSE-5',21)
q6="INSERT INTO Student(Name,Branch,Roll,Section,Age) VALUES({},{},{},{},{})".format('Soumya Das','Computer Science And Engineering',1706273,'CSE-2',21)

a=[q1,q2,q3,q4,q5,q6]

for i in a:
    cur.execute(i)
    con.commit()
print("Queries executed successfully")
