principal = float(input("Enter the amount of principal: "))
annual_interest_rate = (float(input("Enter the annual interest rate: "))) /  100
compounding_periods = float(input("Enter the number of times per year the interes is compounded: "))
time = float(input("Enter the number of years the account will be left to earn interest: "))
future_value = principal * ((1 + annual_interest_rate / compounding_periods) ** (compounding_periods * time))
print("The future value after", format(time, ",.2f"), "years is: $" + format(future_value, ",.2f"))
