Val = int(input("Value:"))
Adder = 0
for C in range(1, Val, 3):
    Adder+=C
    if C%2==0:
        print (C*10)
    else:
        print(C)
print (Adder)
