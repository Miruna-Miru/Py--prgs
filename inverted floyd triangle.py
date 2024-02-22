# INVERTED FLOYD TRIANGLE

ro=int(input("Enter number of rows : "))
in_flo=1
for r in range(ro):
    for cl in range(r-ro,0):
        print(in_flo,end=" ")
        in_flo+=1
    print(" ")
    
    
    
# TRACE OUT
''' ro=4
for r in (ro)       for cl in(r-ro,0)          print(in_flo)                in_flo+=1              print" "
for r in(4)=0       for cl in(0-4,)=-4         print(1)                     in_flo=2
                    for cl in(0-4,)=-3         print(2)                     in_flo=3
                    for cl in(0-4,)=-2         print(3)                     in_flo=4
                    for cl in(0-4,)=-1         print(4)                     in_flo=5
                    for cl in(0-4,)=0 false                                                        print" "
for r in(4)=1       for cl in(1-4,)=-3         print(5)                     in_flo=6
                    for cl in(1-4,)=-2         print(6)                     in_flo=7
                    for cl in(1-4,)=-1         print(7)                     in_flo=8
                    for cl in(1-4,)=0 false                                                        print" "
for r in(4)=2       for cl in(2-4,)=-2         print(8)                     in_flo=9
                    for cl in(2-4,)=-1         print(9)                     in_flo=10
                    for cl in(2-4,)=0 false                                                        print" "
for r in(4)=3       for cl in(3-4,)=-1         print(10)                    in_flo=11
                    for cl in(3-4,)=0 false                                                        print" "
for r in(4)=4 false                             LOOP BREAKS         '''
                    
