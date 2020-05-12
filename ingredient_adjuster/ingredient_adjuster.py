BASE_QUANTITY = 48
SUGAR_CUPS = 1.5
BUTTER_CUPS = 1
FLOUR_CUPS = 2.75
num_cookies = int(input("Enter the number of cookies you want to make: "))
sugar_needed = num_cookies * SUGAR_CUPS / BASE_QUANTITY
butter_needed = num_cookies * BUTTER_CUPS / BASE_QUANTITY
flour_needed = num_cookies * FLOUR_CUPS / BASE_QUANTITY
print("Cups of sugar needed:", format(sugar_needed, ".2f"))
print("Cups of butter needed:", format(butter_needed, ".2f"))
print("Cups of flour needed:", format(flour_needed, ".2f"))
