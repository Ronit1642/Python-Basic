#2+4+8+16+32.............
n=int(input("terms:      "))
s=0
a=2
for i in range(1,n+1):
    a=2**i
    s=s+a
print(s)
