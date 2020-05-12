file_name = input("Enter name of a file: ")

file = open(file_name, "r")

line_number = 1

for line in file:
    line = line.rstrip("\n")
    print(line_number, ": ", line)
    line_number += 1

file.close()
