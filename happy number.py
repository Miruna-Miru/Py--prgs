# HAPPY NUMBER
n=int(input("Enter a number : "))
sum,sum_2,sum_3,sum_4,temp=0,0,0,0,n
s=str(n)
s=len(s)
#print(s)
for lp in range(1,s+1):
    rem=n%10
    sum=sum+rem**2
    n=n//10
#print(sum)
su=str(sum)
su=len(su)
#print(su,"is digits")
for lop in range(1,su+1):
    rem_2=sum%10
    sum_2=sum_2+rem_2**2
    sum=sum//10
t=str(sum_2)
t=len(t)
for loop in range(1,t+1):
    rem_3=sum_2%10
    sum_3=sum_3+rem_3**2
    sum_2=sum_2//10
to=str(sum_3)
to=len(to)
for looop in range(1,to+1):
    rem_4=sum_3%10
    sum_4=sum_4+rem_4**2
    sum_3=sum_3//10
print(sum_4,"is the final sum")
if sum_4==1:
    print(temp,"is a happy number")
else:
    print(f"OOPS!! {temp} is a unhappy number")
    