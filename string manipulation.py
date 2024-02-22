#string manipulaytion
a=input("Enter a word :  ")
print(a.capitalize())
print(a.split("i"))
print(a+" it is a word ")
b=input("Enter the charecter to be searched :  ")
print(a.find(b)," is the index value", a.count(b),"is the count")
print(a.replace("i","*"))
print(a.swapcase())
print(a*2)

