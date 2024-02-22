#PALINDROME OF A NUMBER 
n=int(input("enter a number :"))
rev=0
tem=n#to retain the input we r storing it in temp variable for checking at lastt
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(tem==rev):
    print("the given number is palindrome number ")
else:
    print("the given number is not palindrome")
    
    
    
    
    
    '''      TRACE OUT

it is same as reverse of a number at last the input and proceesed input is compared to check it'''
    
    
    
    
    
    
num=(input("Enter a number : "))
n1=num[::-1]
if num==n1:
    print(num,"is palindrome")
else:
    print(num,"is not a palindrome")