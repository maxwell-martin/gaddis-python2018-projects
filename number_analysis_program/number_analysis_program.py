numbers = []

total = 0

for i in range(1, 21):
    number = float(input("Enter a number for number " + str(i) + ": "))
    total += number
    numbers.append(number)

average = total / len(numbers)

print("Lowest number:", min(numbers))
print("Highest number:", max(numbers))
print("Total:", total)
print("Average:", round(average, 2))
