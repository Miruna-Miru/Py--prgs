a=int(input("enter value for a:"))
b=int(input("enter value for b:"))
c=int(input("enter value for c:"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("none is greater")#executes this only if none of the satement is true