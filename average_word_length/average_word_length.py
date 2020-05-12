word = input("Enter a word: ")

total_chars = 0
total_words = 0

while word != "":
    total_words += 1
    
    for char in word:
        total_chars += 1
    
    word = input("Enter another word or press the enter key to exit: ")

average_length = total_chars / total_words

print("Average length of the words entered:", format(average_length, ".0f"))
