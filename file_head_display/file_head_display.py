file_name = input("Enter name of a file: ")

count = 1

file = open(file_name, mode="r")

for line in file:
    if count > 5:
        break
    line = line.rstrip("\n")
    print(line)
    count += 1

file.close()
