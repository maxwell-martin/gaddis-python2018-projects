SQFT_PER_GAL = 112
HOURLY_PAY_RATE = 35
HOURS_PER_112_SQFT = 8

sqft = float(input("Enter square feet: "))
price_per_gallon = float(input("Enter paint price per gallon: "))

num_gallons_required = sqft / 112
hours_required = (sqft * HOURS_PER_112_SQFT) / SQFT_PER_GAL
paint_cost = num_gallons_required * price_per_gallon
labor_charges = hours_required * HOURLY_PAY_RATE
total_cost = paint_cost + labor_charges

print("Number of gallons of paint required: ", format(num_gallons_required, ",.2f"))
print("Hours of labor required: ", format(hours_required, ",.2f"))
print("Cost of the paint: $", format(paint_cost, ",.2f"), sep="")
print("Labor charges: $", format(labor_charges, ",.2f"), sep="")
print("Total cost of paint job: $", format(total_cost, ",.2f"), sep="")
