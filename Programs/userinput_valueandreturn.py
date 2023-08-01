#user input -  value and return the key
info={1:'a',2:'b',3:'c',4:'d'}
user=input("enter value")
if user in info.values():
    for i in info:
        if info[i]==user:
            print(i)
            break
        
