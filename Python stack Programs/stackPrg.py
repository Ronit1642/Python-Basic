def isEmpty(stk): # checks whether the stack is empty or not
   if stk==[]:
      return True
   else:
      return False

def Push(stk,item): # Allow additions to the stack
   stk.append(item)
   top=len(stk)-1

def Pop(stk):
   if isEmpty(stk): # verifies whether the stack is empty or not
      print("Underflow")
   else: # Allow deletions from the stack
      item=stk.pop()
      if len(stk)==0:
         print("Popped item is "+str(item))
         top=None
      else:
         top=len(stk)
         print("Popped item is "+str(item))

def Display(stk):
   if isEmpty(stk):
      print("Stack is empty")
   else:
      top=len(stk)-1
      print("Elements in the stack are: ")
      for i in range(top,-1,-1):
         print (str(stk[i]))

# executable code

stk=[]
top=None
while True:
     print("Menu \n 1-Display Stack \n 2-Empty Check \n 3-Insert Item\n 4-Delete Item\n 5-Exit\n")
     choice=int(input("Enter Your Choice :"))
     if choice==1:
         Display(stk)
     if choice==2:
         v=isEmpty(stk)
         if v==True:
             print("Stack is empty")
         else:
             print("Stack contains data")
     if choice==3:
         item=int(input("\nEnter element to insert :"))
         Push(stk,item)
     if choice==4:
         Pop(stk)
     if choice==5:
         print("Thank You")
         exit()

   
