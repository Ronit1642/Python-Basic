n=int(input("enter a number"))   
x=len(str(n))

t=n
s=0
v=0
i=0
while(n>0):
    v=n%10
    i=v**x
    s=s+i
    n=n//10
if t==s:
    print("armstrong number")
else:
    print("not an armstrong number")


print("thank you")
    
    
    
