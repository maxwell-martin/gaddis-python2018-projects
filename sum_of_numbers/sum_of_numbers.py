file = open("numbers.txt", mode="r")

total = 0

for line in file:
    total += int(line)

print("Total: ", total)

file.close()
