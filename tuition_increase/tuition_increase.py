PERCENTAGE_INCREASE_PER_YEAR = 0.03

print("Year\tTuition")
print("----------------")

current_tuition = 8000.00

for year in range(1, 6):
    current_tuition *= (1 + PERCENTAGE_INCREASE_PER_YEAR)
    print(year, "\t$", format(current_tuition, ".2f"))
