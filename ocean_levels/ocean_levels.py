RISING_RATE_MM_PER_YR = 1.6

print("Year\tMillimeters Risen")
print("----------------------------")

total_mm_risen = 0.0

for year in range(1, 26):
    total_mm_risen += RISING_RATE_MM_PER_YR
    print(year, "\t", format(total_mm_risen, ".2f"))
