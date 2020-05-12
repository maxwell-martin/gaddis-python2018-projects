import csv

index_dict = {}

with open("Kennedy.txt", "r") as infile:
    reader = csv.reader(infile, delimiter = " ")
    line_num = 1
    for row in reader:
        for word in row:
            if word not in index_dict:
                index_dict[word] = [line_num]
            else:
                if line_num not in index_dict[word]:
                    index_dict[word].append(line_num)
        line_num += 1

keys = []

for key in index_dict.keys():
    keys.append(key)

keys.sort()

with open("index.txt", "w") as outfile:
    for key in keys:
        line = key + ": "
        for line_number in index_dict[key]:
            line += (str(line_number) + " ")
        line = line.rstrip(" ")
        outfile.write(line + "\n")
