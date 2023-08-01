def abc(n):
    count=0
   
    for i in range(1,n+1):
        if n%i == 0:
            count=count+1
    if count == 2:
        print("prime number")
    else:
        print("not an prime number")


n=int(input("enter your favourite number:"))
abc(n)
