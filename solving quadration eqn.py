#solving a quadratic equation 
import cmath #cmath>>>> supports complex number whereas math supports only real numbers 
print("An equation with power 2 is called quadratic equation which is of the form ax^2+bx+c")
a=int(input("Enter value for 'a'  : "))
b=int(input("Enter value for 'b'  : "))
c=int(input("Enter value for 'c'  : "))
dis=b*b-(4*a*c)
sr_dis=cmath.sqrt(dis)
root1=(-b+sr_dis)/2*a
root2=(-b-sr_dis)/2*a
print(f"{root1} {root2}are the roots of the equation {a}x^2+{b}x+{c} ")

