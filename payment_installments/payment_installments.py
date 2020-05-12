TAX = 0.05
purchase_amt = float(input("Enter the amount of a purchase: "))
payment_installments = int(input("Enter the number of payment installments: "))
total = purchase_amt * (1 + TAX)
cost_per_installment = total / payment_installments
print("Total amount of purchase: $" + format(total, ",.2f"))
print("Cost per installment: $" + format(cost_per_installment, ",.2f"))
