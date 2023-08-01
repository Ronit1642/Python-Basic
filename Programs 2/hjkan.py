#wap program using func that will accept an integer and return the equivalent binary of the result.
def n():
    n=int(input(" enter decimal no   :-"))
    a=0
    s=0
    c=1
    while(n>0):
        a=n%2  
        s=s+(a*c)
        c=c*10
        n=int(n/2)
    print(s)

n()
