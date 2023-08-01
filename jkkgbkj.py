a=open("E:\hhhh.txt","r")
b=a.read()
print(b)
a.close()


c=open("E:\hhhh.txt","a+")
d=c.write("p")
c.close()

e=open("E:\hhhh.txt","r")
f=e.read()
print(e)
c.close()


