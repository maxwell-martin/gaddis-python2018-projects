KM_PER_MILE = 1.60934

print("Miles\tKilometers")
print("--------------------")

for miles in range(10, 81, 10):
    km = miles * KM_PER_MILE
    print(miles, "\t", format(km, ".2f"))
