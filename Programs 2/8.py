import os
os.remove("3.txt")




a=open("3.txt","+a")

for i  in range(1,4):
    d=input(" enter your name  ")
    b=input(" enter your marks  ")
    c=str("name="+d+"marks="+b +"\n")
    a.write(c)
a.close()
x=open("3.txt","r")
y=x.read()
print(y)
x.close()
