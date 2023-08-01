def abc(list1,b) :
    print("enter you choice")
    choice = int(input(" 1. Left shift     2. right shift "))
    if choice==1:
        return list1[b:]+list1[:b]
    if choice == 2:
        return list1[-b: : ]+list1[ : :-b]
    if choice >=3:
        return 0
    
    
    
l=list(input("enter items :-  "))
n=int(input("enter no of shifting :) "))

print(abc(l,n))

