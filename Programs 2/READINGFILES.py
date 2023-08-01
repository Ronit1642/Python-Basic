a=open("E:\\hhhh.txt","r")
#b=a.read()
a.seek(4)
b=a.read()
print(b)
print(a.tell())
a.close()



