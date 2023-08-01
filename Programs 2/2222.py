A=eval(input(" enter a numbers"))
B=input("enter the operator like +,-,*,/")
c=A[0]
j=0
for i in range(0,4):
    if(B[j] == "+"):
        c=(c+A[i+1])
        j=j+1
    elif(B[j] == "-"):
        c=(c-A[i+1])
        j=j+1
    elif(B[j] == "*"):
        c=(c*A[i+1])
        j=j+1
    elif(B[j] == "/"):
        c=(c/A[i+1])
        j+=1


print(c)

    
          
