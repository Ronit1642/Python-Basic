file = open('E:\\hhhh.txt', "r")
lines=file.readlines()
file.close()

file=open("E:\\hhhh.txt","w")
file1=open("E:\\abcdef.txt","w")
for line in lines:
    if 'a' in line:
        file1.write(line)
    else:
        file.write(line)
print("file1")
file.close()
file1.close()


