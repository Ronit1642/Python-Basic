t=('a','p','p','l','e')
a=len(t)
c=input("enter string")
if c in t:
    s=0
    print("yes")
    for i in t:
        if i!=c:
            s+=1
        else:
            break
    print(s)
            
            
            

else:
    print("error")


    
