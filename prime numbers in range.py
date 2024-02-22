# PRIME NUMBERS IN RANGE
n=int(input("Enter your lower range : "))
m=int(input("Enter upper range : "))
for x in range(n,m+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=" ")
              
        
          
  