file = open("words.txt", mode="r")

count = 0
longest_word = ""
total_letters = 0

for line in file:
    count += 1
    
    line = line.rstrip("\n")

    letters_old = 0
    for letter in longest_word:
        letters_old += 1
    
    letters_new = 0
    for letter in line:
        letters_new += 1

    if letters_new > letters_old:
        longest_word = line
    
    total_letters += letters_new

average = total_letters / count

print("Number of words in file: ", count)
print("Longest word in file: :", longest_word)
print("Average length of all of the words in the file: ", average)
