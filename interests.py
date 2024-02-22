# INTERESTS
# SIMPLE INTEREST
p=int(input("Enter principle amount : "))
n=int(input("Enter time period in month : "))
r=int(input("Enter rate of interset: "))
sp=(p*n*r)/100
print(sp,"is simple interest")
cp=p*(1+(r/100))**n
print(cp,"is compound interest")


