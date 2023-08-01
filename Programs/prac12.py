import pickle
student_data={}

n=int(input("enter no of students"))
file=open("E:\\abcdef.dat","ab")
for i in range(n):
    student_data["rollno"]=int(input("enter the rollno"))
    student_data["name"]=input("enter the name:")
    student_data["marks"]=float(input("enter student marks:"))
    pickle.dump(student_data,file)
    student_data={}
file.close()

file=open("E:\\abcdef.dat","rb")
try:
    while True:
        student_data=pickle.load(file)
        print(student_data)
except EOFError:
    file.close()
    
found=False
roll_no=int(input("enter the roll no"))
file=open("E:\\abcdef.dat","rb+")
try:
    while True:
        pos=file.tell()
        student_data=pickle.load(file)
        if(student_data["rollno"]==roll_no):
            student_data["marks"]=float(input("enter marks to update"))
            file.seek(pos)
            pickle.dump(student_data,file)
            found=True
except EOFError:
    if(found==False):
        print("Rollno not found")
    else:
        print("marks updated")
    file.close()
    
file=open("E:\\abcdef.dat ","rb")
try:
    while True:
        student_data=pickle.load(file)
        print(student_data)
except EOFError:
    file.close()
