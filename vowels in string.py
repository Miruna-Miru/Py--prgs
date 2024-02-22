#WAY 1
st=input("Enter a string :  ")
st2="aeiouAEIOU"
e,o=0,0
for lp in st:
    if lp in st2:
        e+=1
    else:
        o+=1
print("The number of vowels is : ",e)
print("The number of consonants is : ",o)




#WAY 2
string=input("Enter the string : ")
# v=["a","e","i","o","u"]
count,v1,v2,v3,v4,v5=0,"a","e","i","o","u"
for lp in string:
    #print(lp,end=" ")
   # if lp==v[0] or v[1] or v[2] or v[3] or v[4]:
    if lp==v1 :
        count=count+1
    if lp==v2:
        count=count+1
    if lp==v3:
        count=count+1
    if lp==v4:
        count=count+1
    if lp==v5:
        count=count+1
print(count,"is the total number of vowels in the string")





# WAY 3
vo="aeiou"
s=input("Enter string : ").lower()
c=0
for lp in s:
    if lp in vo:
        c+=1
print("The number of vowels in the enterd string is : ",c)