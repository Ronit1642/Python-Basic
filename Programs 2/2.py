#a=open("1.txt","r")#first file 1.txt reading and storing in a , r is used for extent r=read,w=write(overwriting)
#b=a.read() #read is used for reading the file and value of a is stored in b and then we print the value of b
#print(b)

c=open("1.txt","w")
d=c.write("rLr")
c.close()




w=open("1.txt","r")
d=w.read()
print(d)


