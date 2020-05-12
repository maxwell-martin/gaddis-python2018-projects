STATE_SALES_TAX_RATE = 0.05
COUNTY_SALES_TAX_RATE = 0.025

sales = float(input("Enter total sales for the month: "))

county_sales_tax = sales * COUNTY_SALES_TAX_RATE
state_sales_tax = sales * STATE_SALES_TAX_RATE
total_sales_tax = county_sales_tax + state_sales_tax

print("County sales tax: $", format(county_sales_tax, ",.2f"), sep="")
print("State sales tax: $", format(state_sales_tax, ",.2f"), sep="")
print("Total sales tax: $", format(total_sales_tax, ",.2f"), sep="")
