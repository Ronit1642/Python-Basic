file=open("C:\\Users\\Lenovo\\hhhh.txt", "r")
doc=file.readlines()
for i in doc:
    words=i.split()
    for a in words:
        print(a+"#")
file.close()
