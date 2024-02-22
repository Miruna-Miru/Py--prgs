ro=int(input("how many rows ?:"))
for r in range (ro,0,-1):#we didnt use+1 bcz it will take the input as it is to reduce by one we didnt
    for cl in range (r+1,1,-1):
        print("#",end=" ")
    print("\n")
    
    #TRACE OUT
''' ro=2
r in(ro,1)             cl in(r+1,1)                    row          cloumn
r=1                     cl in(1+1,1)=cl=2              *             *
                        cl =1 sine -1decreased         *
r=0 false sine lower val is itself 1                                 '''