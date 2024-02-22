#
l=int(input("Enter your lower range : "))
u=int(input("Enter your upper range : "))
count=0#initializung the value of count
sum=0
for lp in range (2,u+1):
 if lp>1:
  for lop in range(2,lp):
    if(lp%lop==0):
        count+=1
    if(count==2):
         sum=sum+lp
print(sum,"is sum of prime numbers in the given range")
# else:
#     print(num,"is not a prime number")


    