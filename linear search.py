# LINEAR SEARCH
l=[]
n=int(input("Enter size of the list : "))
for lp in range(1,n+1):
    x=int(input(f"Enter the element {lp} : "))
    l.append(x)
print(l)
s=int(input("Enter value to be searched : "))
f=0
for lp in range(n):
    if s==l[lp]:
        print("The value is found at the position : ",lp)
        f=1
        break
if (f==0):
    print("OOPS!! the value is not available in the list")