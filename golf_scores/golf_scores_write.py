file = open("golf.txt", "w")

go = "y"

while go == "y" or go == "Y":
    name = input("Enter player's name: ")
    score = int(input("Enter player's score: "))
    file.write(name + "\n")
    file.write(str(score) + "\n")
    go = input("Add another? (y = continue): ")

file.close()
