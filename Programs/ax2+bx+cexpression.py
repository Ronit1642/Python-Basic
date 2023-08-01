import cmath
a=int(input("enter a "))
b=int(input("enter b"))
c=int(input("enter c"))
d=((b**2)-(4*a*c))
e=(-b+cmath.sqrt(d))/(2*a)
f=(-b-cmath.sqrt(d))/(2*a)
print(e,"&",f, "are the two roots ")
