#Populate a list(1list only) with the 5 years  values input from the keyboard.
#WAP that prints the no of leap year inputs.


lst=[]
count=0
for i in range(0,5):
    a=int(input("enter years"))
    lst.append(a)
for i in lst:
    if (((i%4 == 0) and (i%100!=0)) or (i%400==0)):
        count=count+1
print(count)

