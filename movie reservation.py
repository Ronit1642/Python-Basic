print('                                               |]*****    #}}}}}}}}]    ^^^   ((((((((((    0000000   &&&&&&&                                                                                                       ')
print('                                               |]         #        }    ^^^   ((            0 * * 0   &                                                           ')
print('                                               |]*****    #********"    ^^^   ((            0 *+* 0   &&&&&&&                                                                  ')
print('                                               |]         #             ^^^   ((            0 * * 0         &                                  ')
print('                                               "--****    #             ^^^   ((((((((((    0000000   &&&&&&&                                                       ')
g=[]
print('                                                                                                                                   ')
print('                                                                                         ')
print('                                                                                               ')
print('                                                             Epicos theatre movie reservation site                                                                       ')
print('                                                             -------------------------------------                                                                       ')
print('                                                                            @   @                                                                                        ')
print('                                                                            *****                                                                                        ')
a=input("Enter your name:")
print("Welcome ",a," to our site.We wish u have a good time ahead!")
print("Movies running:")
print("               1-Minions")
print("               2-Jumanji")
print("               3-Frozen")
print("               4-Jurassic world")
print("               5-Shin chan")
m1="Minions"
m2='Jumanji'
m3='Frozen'
m4='Jurassic world'
m5='Shin chan'
h=int(input("Enter movie code:"))
if h==1:
    b=input("Enter time:")
    c=input("Enter date:")
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    d=int(input("Enter no of seats"))
    for e in range(d):
        f=input("Enter seat no:")
        g.append(f)
    i=input("Enter l for luxury and n for normal:")
    if i=='l':
        j=500
    elif i=='n':
        j=250
    else:
        print('Wrong input!')
    k=int(input("Enter 1 if snacks wanted and 2 for no:") )        
    if k==1:
        print("               1-popcorn")
        print("               2-kfc meal")
        print("               3-mc meals")
        l=int(input("Enter  no:"))
        if l==1:
            m=80
        elif l==2:
            m=270
        elif l==3:
            m=350
        n=(j*d)+m
        print("ur ticket cost is",n)
    else:
        n=j*d
        print("ur ticket cost is",n)
    o=int(input('enter paypal- 1 or credit card-2:'))
    if o==1:
        x=input("paypal id:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       paypal id:",x,"                    |")
        print(" ------------------------------------------")
    elif o==2:
        x=input("credit card id:")
        x1=input("ccv no:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       cc id    :",x,"                    |")
        print("|       ccv id   :",x1,"                   |")
        print(" ------------------------------------------")
    else:
               print('wrong input"')



if h==2:
    b=input("Enter time:")
    c=input("Enter date:")
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    d=int(input("Enter no of seats"))
    for e in range(d):
        f=input("Enter seat no:")
        g.append(f)
    i=input("Enter l for luxury and n for normal:")
    if i=='l':
        j=500
    elif i=='n':
        j=250
    else:
        print('Wrong input!')
    k=int(input("Enter 1 if snacks wanted and 2 for no:") )        
    if k==1:
        print("               1-popcorn")
        print("               2-kfc meal")
        print("               3-mc meals")
        l=int(input("Enter  no:"))
        if l==1:
            m=80
        elif l==2:
            m=270
        elif l==3:
            m=350
        n=(j*d)+m
        print("ur ticket cost is",n)
    else:
        n=j*d
        print("ur ticket cost is",n)
    o=int(input('enter paypal- 1 or credit card-2:'))
    if o==1:
        x=input("paypal id:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       paypal id:",x,"                    |")
        print(" ------------------------------------------")
    elif o==2:
        x=input("credit card id:")
        x1=input("ccv no:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       cc id    :",x,"                    |")
        print("|       ccv id   :",x1,"                   |")
        print(" ------------------------------------------")
    else:
               print('wrong input"')


if h==3:
    b=input("Enter time:")
    c=input("Enter date:")
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    d=int(input("Enter no of seats"))
    for e in range(d):
        f=input("Enter seat no:")
        g.append(f)
    i=input("Enter l for luxury and n for normal:")
    if i=='l':
        j=500
    elif i=='n':
        j=250
    else:
        print('Wrong input!')
    k=int(input("Enter 1 if snacks wanted and 2 for no:") )        
    if k==1:
        print("               1-popcorn")
        print("               2-kfc meal")
        print("               3-mc meals")
        l=int(input("Enter  no:"))
        if l==1:
            m=80
        elif l==2:
            m=270
        elif l==3:
            m=350
        n=(j*d)+m
        print("ur ticket cost is",n)
    else:
        n=j*d
        print("ur ticket cost is",n)
    o=int(input('enter paypal- 1 or credit card-2:'))
    if o==1:
        x=input("paypal id:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       paypal id:",x,"                    |")
        print(" ------------------------------------------")
    elif o==2:
        x=input("credit card id:")
        x1=input("ccv no:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       cc id    :",x,"                    |")
        print("|       ccv id   :",x1,"                   |")
        print(" ------------------------------------------")
    else:
               print('wrong input"')



if h==4:
    b=input("Enter time:")
    c=input("Enter date:")
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    d=int(input("Enter no of seats"))
    for e in range(d):
        f=input("Enter seat no:")
        g.append(f)
    i=input("Enter l for luxury and n for normal:")
    if i=='l':
        j=500
    elif i=='n':
        j=250
    else:
        print('Wrong input!')
    k=int(input("Enter 1 if snacks wanted and 2 for no:") )        
    if k==1:
        print("               1-popcorn")
        print("               2-kfc meal")
        print("               3-mc meals")
        l=int(input("Enter  no:"))
        if l==1:
            m=80
        elif l==2:
            m=270
        elif l==3:
            m=350
        n=(j*d)+m
        print("ur ticket cost is",n)
    else:
        n=j*d
        print("ur ticket cost is",n)
    o=int(input('enter paypal- 1 or credit card-2:'))
    if o==1:
        x=input("paypal id:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       paypal id:",x,"                    |")
        print(" ------------------------------------------")
    elif o==2:
        x=input("credit card id:")
        x1=input("ccv no:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       cc id    :",x,"                    |")
        print("|       ccv id   :",x1,"                   |")
        print(" ------------------------------------------")
    else:
               print('wrong input"')


if h==5:
    b=input("Enter time:")
    c=input("Enter date:")
    print("Please select your seats:")
    print("a1 a2 a3 a4 a5    a6 a7 a8 a9 a10 a11 a12 a13 a14 a15    a16 a17 a18 a19 a20")
    print("b1 b2 b3 b4 b5    b6 b7 b8 b9 b10 b11 b12 b13 b14 b15    b16 b17 b18 b19 b20")
    print("c1 c2 c3 c4 c5    c6 c7 c8 c9 c10 c11 c12 c13 c14 c15    c16 c17 c18 c19 c20")
    print("d1 d2 d3 d4 d5    d6 d7 d8 d9 d10 d11 d12 d13 d14 d15    d16 d17 d18 d19 d20")
    print("e1 e2 e3 e4 e5    e6 e7 e8 e9 e10 e11 e12 e13 e14 e15    e16 e17 e18 e19 e20")
    print("f1 f2 f3 f4 f5    f6 f7 f8 f9 f10 f11 f12 f13 f14 f15    f16 f17 f18 f19 f20")
    print("g1 g2 g3 g4 g5    g6 g7 g8 g9 g10 g11 g12 g13 g14 g15    g16 g17 g18 g19 g20")
    print("                                                                            ")
    print("                                                                            ")
    print("h1 h2 h3 h4 h5    h6 h7 h8 h9 h10 h11 h12 h13 h14 h15    h16 h17 h18 h19 h20")
    print("i1 i2 i3 i4 i5    i6 i7 i8 i9 i10 i11 i12 i13 i14 i15    i16 i17 i18 i19 i20")
    d=int(input("Enter no of seats"))
    for e in range(d):
        f=input("Enter seat no:")
        g.append(f)
    i=input("Enter l for luxury and n for normal:")
    if i=='l':
        j=500
    elif i=='n':
        j=250
    else:
        print('Wrong input!')
    k=int(input("Enter 1 if snacks wanted and 2 for no:") )        
    if k==1:
        print("               1-popcorn")
        print("               2-kfc meal")
        print("               3-mc meals")
        l=int(input("Enter  no:"))
        if l==1:
            m=80
        elif l==2:
            m=270
        elif l==3:
            m=350
        n=(j*d)+m
        print("ur ticket cost is",n)
    else:
        n=j*d
        print("ur ticket cost is",n)
    o=int(input('enter paypal- 1 or credit card-2:'))
    if o==1:
        x=input("paypal id:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       paypal id:",x,"                    |")
        print(" ------------------------------------------")
    elif o==2:
        x=input("credit card id:")
        x1=input("ccv no:")
        print('amount successfully credited!thank u!')
        print("YOUR TICKET:")
        print(" ------------------------------------------")
        print("|       name     :",a,"                    |")
        print("|       date     :",c,'                    |')
        print("|       time     :",b,"                    |")
        print("|       rate     :",n,"                    |")
        print("|       seats    :",g,"                    |")
        print("|       movie    :",h,"                    |")
        print("|       cc id    :",x,"                    |")
        print("|       ccv id   :",x1,"                   |")
        print(" ------------------------------------------")
    else:
               print('wrong input"')
print('thank u for booking through our site.we wish u back to book again!')
l=input("enter end to exit")
if l=='end':
    quit()
else:
    print('tryagain')
    
    l=input("enter end to exit")
    if l=='end':
        quit()
    else:
        print('tryagain')
        
    
            
              
        
        


