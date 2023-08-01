def i1():
    p=int(input("enter principal amount"))
    r= int(input("enter rate of interest"))
    t= int(input(" enter time"))

    return p,r,t
p,r,t= i1()
   

def fact():
    si=p*r*t
    final=si/100
    return final
final=fact()

print(final)   

