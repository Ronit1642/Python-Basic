a=open("3.txt","+a")#append function is used 
b=a.write(input(" enter the value :- "))
a.close()

c=open("3.txt","r")
d=c.read()
print(d)
c.close()
