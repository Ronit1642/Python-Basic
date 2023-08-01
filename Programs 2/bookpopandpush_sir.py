##############   STACK IMPLIMENTION   ##############
"""
    Stack:implemented as a list
    top : integer having position of topmost element in the Stack
"""
def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if(isEmpty(stk)):
        return "Underflow"
    else:
        item=stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if(isEmpty(stk)):
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if(isEmpty(stk)):
        print("Stack empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
#_main_
Stack=[]             #initially stack is empty
top=None
while True:
    print("=====STACK OPERATIONS=====")
    print("1.Push\n2.Pop\n3.Peek\n4.Display stack\n5.Exit")
    ch=int(input("Enter your choice form 1 to 5 : "))
    if(ch==1):
        print("==============INPUT==============")
        item=int(input("Enter item : "))
        print("=================================")
        Push(Stack,item)
    elif(ch==2):
        item=Pop(Stack)
        if(item=="Underflow"):
            print("==============OUTPUT==============")
            print("Underflow! stack is Empty!")
            print("==================================")
        else:
            print("==============OUTPUT==============")
            print("Popped item is",item)
            print("==================================")
    elif(ch==3):
        item=Peek(Stack)
        if(item=="Underflow"):
            print("==============OUTPUT==============")
            print("Underflow! stack is Empty!")
            print("==================================")
        else:
            print("==============OUTPUT==============")
            print("Topmost item is",item)
            print("==================================")
    elif(ch==4):
        print("==============OUTPUT==============")
        Display(Stack)
        print("==================================")
    elif(ch==5):
        break
    else:
        print("==============OUTPUT==============")
        print("Invalid choice!")
        print("==================================")
