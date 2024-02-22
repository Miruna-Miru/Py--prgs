n=int(input("enter a year :  "))
if (n %100!=0 or n%400==0) and n%4==0:
      print(f"{n} is a leap year")
else:
     print(f"{n} is not a leap year")
