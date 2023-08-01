# 0 1 1 2 3 5 8 13 21 34
n=int(input("enter terms :- "))
a,b=0,1
print(a)
print(b)
for i in range(1,n-1):
    a,b=b,a+b
    print(b)
    

    
