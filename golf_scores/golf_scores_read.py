file = open("golf.txt", "r")

name = file.readline()

while name != "":
    name = name.rstrip("\n")
    score = file.readline()
    score = score.rstrip("\n")
    print(name, "-", score)
    name = file.readline()

file.close()
