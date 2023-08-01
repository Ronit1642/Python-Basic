#write a push and pop any no/name method in python
choice=int(input("enter your choice"))
lst=[4,5,7,5]
print(lst)
if (choice == 1):
    a=int(input(" enter last element "))
    lst.append(a)
    print(lst)
    

elif choice == 2:
    lst.pop()
    print(lst)

else:
    print("error")
