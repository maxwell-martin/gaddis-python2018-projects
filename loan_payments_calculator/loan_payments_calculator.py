def calc_payment(r, a, m):
    return (r * a) / (1 - ((1 + r) ** -m))

loan_amt = float(input("Enter loan amount: "))
monthly_interest_rate = float(input("Enter monthly interest rate (%): ")) / 100
months = int(input("Enter number of months: "))

payment = calc_payment(monthly_interest_rate, loan_amt, months)

print("Loan payment per month: $", format(payment, ",.2f"), sep="")

