def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
num=int(input("enter the number"))
print("the factorial of the",num,"is",fact(num))
