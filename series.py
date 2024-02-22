 #  SERIES
 # Sum of squares
'''print("This program finds the su of series of the form 1+2^2+3^2+4^2+5^2.......")
n=int(input("Enter number : "))
tot=0
for lp in range(1,n+1):
     lp=lp**2
     print(lp,end=" ")
     tot+=lp
print("\nSum is : ",tot)'''


# TRACE OUT
''' n = 3, tot =0
for lp in(1,4)               lp**2              print(lp)             tot+=lp                     print("SUM" ,tot)
for lp in(1,4)=1             1**2=1              1                     0+1=1
for lp in(1,4)=2             2**2=4              4                     1+4=5
for lp in(1,4)=3             3**2=9              9                     5+9=14
for lp in(1,4)=4 false                                                                            SUM: 14 '''




# Sum of cubes
'''print("This program finds the su of series of the form 1+2^3+3^3+4^3+5^3.......")
n=int(input("Enter number : "))
tot=0
for lp in range(1,n+1):
     lp=lp**3
     print(lp,end=" ")
     tot+=lp
print("\nSum is : ",tot)'''


# TRACE OUT
'''n = 4, tot =0
for lp in(1,5)               lp**3              print(lp)             tot+=lp                     print("SUM" ,tot)
for lp in(1,5)=1             1**3=1              1                     0+1=1
for lp in(1,5)=2             2**3=8              8                     1+8=9
for lp in(1,5)=3             3**3=27             27                    9+27=36
for lp in(1,5)=4             4**3=64             64                    36+64=100
for lp in(1,5)=5 false                                                                             "SUM :100'''



# Sum of factorial series
'''print("This is to find sum of series of the form 1!+2!+3!+4!+5!+.....")
n=int(input("Enter n : "))
su,fac=0,1
for lp in range(1,n+1):
    fac*=lp
    lp+=1
    print(fac,end=" ")
    su+=fac
print("\n Sum of the series is : ",su)'''