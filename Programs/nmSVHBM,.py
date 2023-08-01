import area
import circum
import recper
import recarea

print("1. 	Area of a Circle")
print("2.   Circumference of Circle")
print("3.   Area of Rectangle")
print("4.   Perimeter of Rectangle")

choice=int(input("enter the choice"))
if choice==1:
    print("the area of circle is",area. area_circle())
    
elif choice==2:
    print("circumference of circle",circum.curcum_circle())

elif choice==3:
    print("the area of rectangle is ",recarea.rec_area())
    
elif choice==4:
    print("the perimeter of rectangle is ",recper.rec_perimeter())
    
    
else:
    print("enter valid choice")
