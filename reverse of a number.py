#reverse of a number
num=int(input("enter a number:"))
rev=0
temp=num
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print("reverse of a number is :",rev,"it is pALINDROME")
    
else:
    print("OOPS! it is not a palindrome")





''' TRACE OUT
num=234
 
whilenum!=0          rem=num%10                rev=rev*10+rem                num=num//10              print
234!=0 tr            rem=234%10 =4             rev=0*10+4=4                  num=234//10=23
23!=0 tr             rem=23%10  =3             rev=4*10+3=43                 num=23//10=2
2!=0  tr             rem=2%10   =2             rev=43*10+2=432               num=2//10=0
0!=0  fl                                       COMES OUT OF THE LOOP                                  432'''