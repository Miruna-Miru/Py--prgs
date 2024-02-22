# BINARY SEARCH
l=[]
n=int(input("Enter size of the list : "))
for lp in range(1,n+1):
    x=int(input(f"Enter the element {lp} : "))
    l.append(x)
print(l)
for lp in range(n):
    for lop in range(lp+1,n):
        if l[lp]>l[lop]:
            tem=l[lp]
            l[lp]=l[lop]
            l[lop]=tem
print(l,"Is the sorted list")
s=int(input("Enter the value to be searched : "))
be=0
end=n-1
f=False
for lp in range(n):
    while be<=end and not f:# not f means f becomes true
        mid=(be+end)//2
        if(s==l[mid]):
            f=True
            break
        elif(s<l[mid]):
            end=mid-1
        else:
            be=mid+1
if f==True:
     print("The value is found at the position : ",lp-1)
else:
    print("OOPS!! the value is not in the created list")
