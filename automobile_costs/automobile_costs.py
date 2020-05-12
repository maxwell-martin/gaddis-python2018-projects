loan_payment = float(input("Enter monthly loan payment: "))
insurance = float(input("Enter monthly insurance payment: "))
gas = float(input("Enter monthly gas payment: "))
oil = float(input("Enter monthly oil payment: "))
tires = float(input("Enter monthly tires payment: "))
maintenance = float(input("Enter monthly maintenance payment: "))

total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

print("Total monthly cost: $", format(total_monthly_cost, ",.2f"), sep="")

total_yearly_cost = total_monthly_cost * 12

print("Total annual cost: $", format(total_yearly_cost, ",.2f"), sep="")
