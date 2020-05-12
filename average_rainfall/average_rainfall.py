years = int(input("Enter the number of years: "))

num_months = 0
total_rainfall = 0.0

for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall_inches = float(input("How much did it rain in inches in month " +
                                  str(month) + ", year " + str(year) + "? "))
        num_months += 1

        total_rainfall += rainfall_inches

print("Number of months:", str(num_months))
print("Total inches of rainfall:", str(format(total_rainfall, ".2f")))
print("Average rainfall per month:", str(format(total_rainfall / num_months, ".2f")))
