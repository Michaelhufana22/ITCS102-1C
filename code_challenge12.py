for M in range(1,11,1) :
    for I in range(10,M,-1) :
        print(" ",end= " " )
    for C in range(1,M,1):
        print("*",end= " ")
    for H in range(1,M,1) :
        print("*",end= " ")
    print()
for M in range(1,11,1) :
    for I in range(1,M,1) :
        print(" ",end= " " )
    for C in range(10,M,-1):
        print("*",end= " ")
    for H in range(10,M,-1) :
        print("*",end= " ")
    print()