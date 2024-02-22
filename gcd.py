def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=int(input("Enter number : ")),int(input("Enter number2 : "))
print(gcd(a,b),f"is the gcd of {a} and {b}")