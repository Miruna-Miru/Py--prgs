# factors of a number
num=int(input("enter a number:"))
print("the factors of ",num,"are")
for fac in range(1,num+1):#num+1 bcz the factors are always smaller than the num not greater than it
    if(num%fac==0):
        print(fac)
         
         
         


