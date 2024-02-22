#AMSTRONG NUMBER
num=int(input("enter the number:"))
#n=int(input("enter the no of digits in the given number:"))
n=len(str(num))#len is used to find the lenght ,str means string ie num 
sum=0
temp=num
while temp!=0:
    ind=temp%10
    sum=sum+ind**n
    temp=temp//10
if(num==sum):
    print(num,"is the amstrong number")
else:
    print(num,"is not a amstrong number:")