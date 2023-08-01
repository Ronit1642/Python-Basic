info={1:'a',2:'b',3:'c',4:'d'}
user=input("enter value")
for i in info:
        if info[i].lower()==user.lower():
            print(i)
            break
else:
    print("error")
        
        
