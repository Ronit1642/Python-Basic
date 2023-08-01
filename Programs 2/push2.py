a=int(input("enter a limit"))
b=0
lst=[]

def dis():
    print(lst)
def ph():
    c=int(input(" enter push element "))
    lst.append(c)
def pp():
    lst.pop()
while(b<a):
    print("1. Display \n 2.Push \n 3. POP   ")
    choice=int(input("enter your choice"))
    if choice == 1:
        dis()
    elif choice == 2:
        ph()
    elif choice == 3:
        pp()
    b=b+1


    
