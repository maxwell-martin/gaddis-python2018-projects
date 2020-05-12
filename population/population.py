organisms = int(input("Starting number of organisms: "))
average_daily_increase = (float(input("Average daily increase (%): "))) / 100
num_days_to_multiply = int(input("Number of days to multiply: "))

print("Day Approximate\t\tPopulation")
print("----------------------------------------")

for day in range(1, num_days_to_multiply + 1):
    print(day, "\t\t\t", organisms, sep="")
    organisms *= (1 + average_daily_increase)
