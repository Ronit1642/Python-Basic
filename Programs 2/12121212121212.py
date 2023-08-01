def arm():
    n=int(input("enter no"))
    temp=n
    def xyz(a):
        sum=0
        while a>0:
            digit=a%10
            sum=sum+digit**3
            a=a//10
        return sum
    m=xyz(temp)
    if n == m:
        print("armstrong number")
    else:
        print("not an armstrong number")

arm()
