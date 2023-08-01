def palin(x):
    n=x[ : :-1]
    if x==n:
        print("palindrome")
    else:
        print(":no:")  
x=input("enter string")
palin(x)
