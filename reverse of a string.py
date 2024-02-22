#reverse of a string
s=input("Enter a string   : ")
se = s[::-1]
print(se,"is the reverse of given string")
if s == s[::-1]:
    print("The given string is palindrome")
else:
    print("OOPS!!!! it is not palindrome")