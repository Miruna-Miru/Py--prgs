# A Number is fibannoci number or not
n=int(input("Enter a number :  "))
a,b,c=1,1,0
if n==0 or n==1:
    print("It is a fibanocci number")
else:
    while c<n:
        c=a+b
        a=b
        b=c
    if c==n:
            print("It is a fibannoci number")
    else:
            print("It is not a fibannoci number ")