s=open("word.py")
x=s.read()
long=" "
a=x.split(" ")
for lp in a:
    if len(lp)>len(long):
        long=lp
print(long, "IS THE LONGEST WORD")
'''short=" "
for lp in a:
    if len(lp)<len(long):
        short=lp
print(short , "IS THE SHORTEST WORD")'''# Some error is there
n=input("Enter word to be searched : ")
if n in x:# here x is used since the s is read in x 
          print("Yes it is found : " ,lp)
             break
else:
    print("OOPS!!! it is not there")
x=s.close()