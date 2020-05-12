file = open("scores.txt", mode="r")

count = 0
highest_score_name = ""
highest_score_value = 0

name = file.readline()

while name != "": 
    name = name.rstrip("\n")
    score = int(file.readline())

    if score > highest_score_value:
        highest_score_name = name
        highest_score_value = score

    name = file.readline()

print("Highest Score: ", highest_score_name, "-", highest_score_value)

file.close()
