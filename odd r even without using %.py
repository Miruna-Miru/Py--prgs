#ODD R EVEN WITHOUT %
#USING FLOOR division//
num=int(input("enter the number:"))
if (num//2)*2==num:
    print(num,"is a even number")
else:
    print(num,"is odd number")
    
    
    
#USING SHIFT
low=int(input("enter the lower limit:"))
hig=int(input("enter the upper limit:"))
for lp in range(low,hig+1):
    if(lp>>1)<<1==lp:
        print(lp,"is even")
        break
    else:
        print(lp,"is odd")