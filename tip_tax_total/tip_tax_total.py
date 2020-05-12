TIP_PERCENTAGE = 0.18
SALES_TAX = 0.07
subtotal = float(input("What is the food charge? "))
tax_amt = subtotal * SALES_TAX
tip = (subtotal + tax_amt) * TIP_PERCENTAGE
total = subtotal + tax_amt + tip
print("Subtotal: \t$" + format(subtotal, ",.2f"))
print("Tax Amount: \t$" + format(tax_amt, ",.2f"))
print("Tip Amount: \t$" + format(tip, ",.2f"))
print("Total: \t\t$" + format(total, ",.2f"))
