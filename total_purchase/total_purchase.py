SALES_TAX_PERCENTAGE = 0.07
item1 = float(input("What is the price of item 1? "))
item2 = float(input("What is the price of item 2? "))
item3 = float(input("What is the price of item 3? "))
item4 = float(input("What is the price of item 4? "))
item5 = float(input("What is the price of item 5? "))
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * SALES_TAX_PERCENTAGE
total = subtotal + sales_tax
print("Subtotal: \t$" +  format(subtotal, ",.2f"))
print("Sales Tax: \t$" + format(sales_tax, ",.2f"))
print("Total: \t\t$" + format(total, ",.2f"))
