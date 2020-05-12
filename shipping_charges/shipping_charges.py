TWO_LESS = 1.50
TWO_SIX = 3.00
SIX_TEN = 4.00
TEN_PLUS = 4.75

pkg_weight = float(input("Enter the weight of the package in pounds: "))

total = 0.0

if pkg_weight <= 2:
    total = pkg_weight * TWO_LESS
    print("Total cost: $", format(total, ",.2f"), sep="")
elif pkg_weight > 2 and pkg_weight <= 6:
    total = pkg_weight * TWO_SIX
    print("Total cost: $", format(total, ",.2f"), sep="")
elif pkg_weight > 6 and pkg_weight <= 10:
    total = pkg_weight * SIX_TEN
    print("Total cost: $", format(total, ",.2f"), sep="")
else:
    total = pkg_weight * TEN_PLUS
    print("Total cost: $", format(total, ",.2f"), sep="")
