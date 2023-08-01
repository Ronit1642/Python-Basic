def isEmpty(stk):
    if(stk == []):
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isEmpty(stk): 
        return "Underflow"
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
        if isEmpty(stk):
            print("stack empty")
        else:
            top=len(stk)-1
            print(stk[top],"<-top")
            for a in range(top-1,-1,-1):
                print(stk[a])


Stack=[]
top = None
while True:
    print("stack operations")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display stack")
    print("5.exit")

    ch=int(input("enter your choice(1-5) : "))
    if ch == 1:
        item = int(input("enter item"))
        Push(Stack,item)
    if ch == 2:
        item = Pop(Stack)
        if item == "Underflow":
            print("Underflow,stack is empty")
        else:
            print("popped item is ",item)

    elif ch == 3:
        item =Peek(Stack)
        if item == "Underflow":
            print("Underflow,stack is empty")
        else:
            print("toppmost item is ",item)
    elif ch == 4:
        Display(Stack)
    elif ch == 5:
         break
    else:
         print("invalid choice")
        



    
    







        
    
