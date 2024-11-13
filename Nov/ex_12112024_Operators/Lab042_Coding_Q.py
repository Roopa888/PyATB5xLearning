# Program to print the area of a circle
#Take radius as inout from the user and take pi =3.14 and Calculate the area using the formula pi*r(**2)
#Step1=logic building -Confirm the input and o/p
#radius--->float
# pi--->3.14
# power--->either math.pow() or "**"
#o/p=float whcih is teh area and print the area
# Step2-Rough logic
# area=3.14*(r**2)
# Step3-Actual code to produce the results
import math

radius=float(input("Enter the radius\n"))
print(radius)
area=3.1456789*(radius**2)
print("Area of the circle is ",area)

print(f"Area of the circle is (Area):{area}")
#Using formatting .Suppose there are many decimal places in the result(if we take pi as 3.1456789)
# and if we want to restrict it to 2 decimal we can do that
# eg {area}.2f
print(f"Area of the circle is (Area):{area:.3f}")
print("Using pow function")
area=3.14*pow(radius,2)
print("Area of the circle is ",area)

# We can use the math.pi and math.pow also in the above calculation after importing math
print("Using Math.Pi and Math.pow")
print(math.pi)#automatically imported math in line11 when we wrote this line
area=math.pi*math.pow(radius,2)# ya can be ignored
print(area)
##Upto line 32 can be replaced with a single line program as below ,but not recommented
print("Single line input and results .See below")
print(3.14*(float(input("Enter the radius\n"))**2))

#Other math functions
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
print(math.pow(3,2))
