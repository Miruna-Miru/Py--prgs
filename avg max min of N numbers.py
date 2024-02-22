n=int(input("how many numbers you are going to enter:"))
sum=0
for lp in range(1,n+1):
    num=int(input(f"enter number {lp} :"))
    if lp==1:
        max=num
        min=num
    if num>max:
        max=num
    #if num<min:
    else :
        min=num
    sum=sum+num
avg=sum/n
print(f"the maximum number is {max}")
print("the minimum number is",min)
print(f"the average of {n} numbers is ",avg)