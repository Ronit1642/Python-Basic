a=int(input("enter 1st no"))
b=int(input("enter 2st no"))
c=int(input("enter 3rd no"))
if(a>b>c):
    print(a,">",b,">",c)
elif(a>c>b):
    print(a,">",c,">",b)
elif(b>c>a):
    print(b,">",c,">",a)
elif(b>a>c):
    print(b,">",a,">",c)
elif(c>a>b):
    print(c,">",a,">",b)
else:
    print(c,">",b,">",a)


    
