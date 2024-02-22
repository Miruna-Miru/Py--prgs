#summ of even and odd
s=int(input("enter your starting range:"))
e=int(input("enter your ending range:"))
even =0
odd =0
for num in range(s,e+1):
    if num%2==0:
        even=even+num
        #print(even)
    
    else:
        odd=odd+num
        #print(odd)
print(even,"is the sum of all even numbers  between",s,"and",e)
print(odd,"is the sum of all  odd numbers between",s,"and",e)