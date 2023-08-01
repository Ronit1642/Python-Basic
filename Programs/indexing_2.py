#given two strings create a new string by appending second string into the middle of first string
a="physics"
b="math"
c=int(len(a)/2)
d=a[:c:]+b+a[c: : ]
print(d)
