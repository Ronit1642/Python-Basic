def abc(dec_num):
    print("enter the choice")
    choice=int(input("1.binary 2.octal 3.hexa"))
    if choice==1:
        return bin(dec_num)
    if choice == 2:
        return oct(dec_num)
    if choice == 3:
        return hex(dec_num)
    else:
        print("error")        
        
        

dec_num=int(input("enter the decimal number"))
print(abc(dec_num))           
