file = open("words.txt", mode="w")

number = int(input("How many words would you like to write to a file? "))

for i in range(number):
    word = input("Enter word #" + str(i + 1) + ": ")
    file.write(word + "\n")

file.close()
