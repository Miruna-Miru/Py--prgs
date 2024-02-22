# DELETING DUPLICATES IN A LIST
li=[]
l=[]
n=int(input("How many elements to be stored?   "))
for lp in range(1,n+1):
    x=int(input(f"Enter element {lp} :  "))
    li.append(x)
print(li,"is the created list ")
for lop in li:
    if lop not in l:
        l.append(lop)
print(l)



# DELETING DUPLICATE IN STRING AND INT BCZ WE HAVENT USED INT FUN IN GETTING INPUT FROM USER
n=input("Enter a string : " )
ls=[]
st=""
for lp in n:
    if lp not in ls:
        ls.append(lp)
st=st.join(ls)
print(st)