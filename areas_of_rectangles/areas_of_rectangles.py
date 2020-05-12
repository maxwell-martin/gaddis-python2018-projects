length_1 = float(input("Enter length of rectangle 1: "))
width_1 = float(input("Enter width of rectangle 1: "))
length_2 = float(input("Enter length of rectangle 2: "))
width_2 = float(input("Enter width of rectangle 2: "))

area_1 = length_1 * width_1
area_2 = length_2 * width_2

if area_1 > area_2:
    print("Rectangle 1 has a greater area.")
elif area_1 < area_2:
    print("Rectangle 2 has a greater area.")
else:
    print("The rectangles have the same area.")
