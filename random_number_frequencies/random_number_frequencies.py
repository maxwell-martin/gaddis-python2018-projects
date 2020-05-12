import random

numbers = {}

for i in range(100):
    num = random.randint(1, 10)
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1

print("Number\tFrequency")
print("------------------")

total_frequency = 0

for num in numbers:
    print(num, "\t", numbers[num])
    total_frequency += numbers[num]

print("Total frequency:", total_frequency)
