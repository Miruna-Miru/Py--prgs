# using recursion
def fac(n):
    if n==1:
        return n
    elif  n==0:
        return 1
    else:
        return n * fac(n-1)
n=int(input("Enter a number to find factorial :  "))
print(fac(n))



# WITHOUT USING RECURSION
n=int(input("Enter a number : "))
fac=1
if n== 1 or n==0:
    print("THE factorial is : 1")
else:
    for lp in range(1,n+1):
        fac*=lp
print(fac)
