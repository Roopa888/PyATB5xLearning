# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal)
# Logic building
# Step1
# i/p->s1, s2, s3 → int
#
# o/p →. iso, eq, scelene
from turtledemo.sorting_animate import isort

side1 = input("Enter length of  side1 of the triangle\n")
side2 = input("Enter length of  side2 of the triangle\n")
side3 = input("Enter length of  side3 of the triangle\n")
# Step#-Rough logic
#  side1=side2=side3-->eq
# side1 = side2 or side2==side3 or side1==side3 -->iso
# side1!=side2!=side3---> scelene

# Actual code
if side1 == side2 == side3:
    print("Triangle classification-side1 and side2 and side3 are equal: eq")
elif side1 == side2:
    print("Triangle classification-side1 and side2 are equal: iso")
elif side1 == side3:
    print("Triangle classification-side1 and side3 are equal: iso")
elif side2 == side3:
    print("Triangle classification -side2 and side3 are equal: iso")
else:
    print("Triangle classification -side1 ,side3 and side3 are not equal: scelene")
