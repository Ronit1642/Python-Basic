#x-x2+x3-x4+x5...
#5
x=int(input("terms:      "))
s=0
for i in range(1,x+1):
    s+=(x**i)*((-1)**(i-1))
print(s)
