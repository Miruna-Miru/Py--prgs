#to find sum of digits of a number
n=int(input("How many digit number are you going to enter?"))
num=int(input("Enter a number :"))
sum1,add=0,0
for lp in range(1,n+1):
    rem=num%10
    sum1=sum1+rem
    num=num//10
print(sum1,"is the initial sum")
tot=str(sum)#converting it to str bcz len can be used only for string
#print(len(tot))
#@print(le,"is the lenth of the first sum value")
for lp2 in range(1,len(tot)+1):
    remi=sum1%10
    add=add+remi
    sum1=sum1//10
print(add,"is the final sum")
    
    
