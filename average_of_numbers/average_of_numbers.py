file = open("numbers.txt", mode="r")

total = 0
count = 0

for line in file:
    total += int(line)
    count += 1

average = total / count

print("Average: ", average)

file.close()
