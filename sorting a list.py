#sorting a list
n=int(input("How many terms?  "))
lst=[]
for lp in range (1,n+1):
    val=int(input(f"Enter your {lp} index number :  "))
    lst.append(val)
print(lst,"is the list you have created ")
lst.sort()
print(lst,"is the sorted list ")



# way 2
#sorting a list
al=[]
n=int(input("Enter total number of elements : "))
for lp in range (1,n+1):
    num=int(input(f"Enter your number {lp}: "))
    al.append(num)
print(al,"is the original list")
for lop in range(1,n+1):
    for loop in range(lop+1,n):
        if al[lop]>al[loop]:
            tem=al[lop]
            al[lop]=al[loop]
            al[loop]=tem
print(al)





#WAY 3
li=[]
nli=[]
n=int(input("How many terms are you going to enter ? "))
for lp in range(1,n+1):
    x=int(input(f"Enter element{lp} :  "))
    li.append(x)
print(li,"is the created list")
while li:
    min=li[0]
    for lop in li:
        if lop <min:
            min = lop
    nli.append(min)
    li.remove(min)
print(nli)