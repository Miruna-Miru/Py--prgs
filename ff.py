#to find smallest  largest of the list
n=int(input("Enter total number of inputs you are going to give : "))
lst=[]
for lp in range(1,n+1):
    x=int(input(f"Enter the value {lp} :  "))
    lst.append(x)
print(lst,"is created")
lar,smal=lst[0],lst[0]
for lop in range(0,n+1):
    if lar<lst[lop]:
        lar=lst[lop]
    if smal>lst[lop]:
        smal=lst[lop]
print(lar," is the larget")
print(smal,"is the smallest")
    
    