#a=open("3.txt","r")
#b=a.read()
#print(b)

c=open("3.txt","w")
b=c.write("ronit")
c.close()
a=open("3.txt","r")
b=a.read()
print(b)
a.close()
