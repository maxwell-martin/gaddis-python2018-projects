numbers_file = open("numbers.txt", mode="r")

for line in numbers_file:
    line = line.rstrip("\n")
    print(line)

numbers_file.close()
