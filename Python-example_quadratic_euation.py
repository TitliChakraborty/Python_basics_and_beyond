import math
print("Enter the Co-efficient of the equation ax^2+bx+c=0")
a=float(input("Enter value of a "))
b=float(input("Enter value of b "))
c=float(input("Enter value of c "))
print(f"the equation is: {a}x^2 +{b}x + {c}")
dis=b**2-4*a*c
if(dis<0):
    print("Roots are not real")
else:
    x1= (-b+ math.sqrt(dis))/2*a
    x2= (-b- math.sqrt(dis))/2*a
    print(f"Rooots of the equations are {x1} and {x2}")
