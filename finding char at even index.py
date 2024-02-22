# FINDING EVEN CHAR IN STRING
def ev_st(s):
 for lp in range(len(s)):
    if lp%2==0:
       print(s[lp],end=" ")
    else:
        continue
s=input("Enter a string : ")
ev_st(s)

    