rainfall = []

for month in range(1,13):
    rainfall.append(float(input("Enter rainfall for month " + str(month) + ": ")))

total = 0
for entry in rainfall:
    total += entry

average = total / len(rainfall)

min_month = rainfall.index(min(rainfall)) + 1
max_month = rainfall.index(max(rainfall)) + 1

print("Total rainfall: ", round(total, 2))
print("Average monthly rainfall: ", round(average, 2))
print("Month with lowest amount: ", min_month)
print("Month with highest amount: ", max_month)
