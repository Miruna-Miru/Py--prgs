#  RIGHT SIDED INVERTED FLOYD TRIANGLE
n=int(input("Enter number of rows : "))
a=1   
for r in range(0,n+1):
   # a=1 if it is declared here the value change from 1 to the no of iteration, that is you get 1 as starting value for each row
    for c in range(0,n):
        if c>=n-r:
            print("#",end=" ")
            a+=1
        else:
            print(" ",end=" ")
    print(" ")
    
    
    
    