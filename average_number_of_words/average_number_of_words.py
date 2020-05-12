with open("text.txt", "r") as infile:
    total_words = 0
    total_sentences = 0
    for line in infile:
        total_sentences += 1
        words = line.split()
        for word in words:
            total_words += 1

average = total_words / total_sentences

print("Average number of words per sentence:", round(average, 2))
