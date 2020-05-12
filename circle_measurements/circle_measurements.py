import math

radius = float(input("Enter the radius of a circle: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("Area:", format(area, ".2f"))
print("Circumference:", format(circumference, ".2f"))
