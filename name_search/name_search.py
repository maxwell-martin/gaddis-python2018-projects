boys = []
girls = []

with open("BoyNames.txt") as boy_infile:
    for line in boy_infile:
        boys.append(line.rstrip("\n"))

with open("GirlNames.txt") as girl_infile:
    for line in girl_infile:
        girls.append(line.rstrip("\n"))

boy = input("Enter a boy's name, or press enter to skip: ")
girl = input("Enter a girl's name, or press enter to skip: ")

if boy != "":
    if boy in boys:
        print(boy, "is among the most popular boy names.")
    else:
        print(boy, "is not among the most popular boy names.")

if girl != "":
    if girl in girls:
        print(girl, "is among the most popular girl names.")
    else:
        print(girl, "is not among the most popular girl names.")
