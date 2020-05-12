import random

even_count = 0
odd_count = 0

for i in range(100):
    random_number = random.randint(1, 250)
    if random_number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
