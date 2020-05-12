PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

amt_pennies = (int(input("Enter the number of pennies: "))) * PENNY
amt_nickels = (int(input("Enter the number of nickels: "))) * NICKEL
amt_dimes = (int(input("Enter the number of dimes: "))) * DIME
amt_quarters = (int(input("Enter the number of quarters: "))) * QUARTER

total = amt_pennies + amt_nickels + amt_dimes + amt_quarters

if total == 1.00:
    print("You won!")
elif total > 1.00:
    print("The amount entered was over $1.00")
else:
    print("The amount entered was under $1.00")
