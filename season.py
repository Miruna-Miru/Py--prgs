# SEASON
d=int(input("Enter date : "))
m=int(input("Enter month: "))
if (m==1 and 1<=d<=31) or (m==2 and 1<=d<=28) or (m==3 and 1<=d<=21):
    print("It is SPRING")
elif (m==4 and 1<=d<=30) or (m==5 and 1<=d<=31) or (m==6 and 1<=d<=21):
    print("It is SUMMER")
elif (m==6 and 22<=d<=30) or (m==7 and 1<=d<=31) or (m==8 and 1<=d<=30) or (m==9 and 1<=d<=22):
    print("It is FALL")
else:
    print("It is WINTER")
    