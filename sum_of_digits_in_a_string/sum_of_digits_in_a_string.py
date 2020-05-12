numbers = input("Enter a series of single-digit numbers with nothing" +
                " separating them: ")

total = 0

for num in numbers:
    num = int(num)
    total += num

print("Total:", total)
