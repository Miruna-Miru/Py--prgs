ro=int(input("how many rows ?:"))
floy=1
for r in range  (ro):
    for cl in range(r+1):
        print(floy,end=" ")
        floy=floy+1
    print("\n")
    
    
    
    #TRACE OUT not clear tarce out 
    
'''  ro=4
 r in (ro)                     cl in(r)             print(floy)            floy+=
 r in (4)=0                     cl in(1)=0            1                       2
 rin(4) =1                      cl=1                 2                       3
 r in (4)=2                     cl=2                 3                       4
 r in (4)=3                     cl=3                4                        5
 r in (4) =4 flse'''