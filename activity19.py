for M in range(1,11,1) :
    for I in range(10,M,-1) :
        print(" ",end= " " )
    for C in range(1,M,1):
        print("*",end= " ")
    for H in range(1,M,1) :
        print("*",end= " ")
    print()
#other half
for A in range(1,11,1) :
    for E in range(1,A,1) :
        print(" ",end=" ")
    for L in range(10,A,-1) :
        print("*",end=" ")
    for O in range(10,A,-1) :
        print("*",end = " ")
    print()



 