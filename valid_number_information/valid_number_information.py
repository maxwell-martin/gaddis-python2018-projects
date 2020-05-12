numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

valid_numbers = []

for i in range(101):
    if i in numbers:
        valid_numbers.append(i)

total = 0
for num in valid_numbers:
    total += num

average = total / len(valid_numbers)

print("Total: ", total)
print("Average: ", round(average, 2))
