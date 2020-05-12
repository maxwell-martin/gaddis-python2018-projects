unique_words = set()

with open("words.txt", "r") as infile:
    count = 0
    for word in infile:
        count += 1
        unique_words.add(word.rstrip("\n"))

print("Total words:", count)
print("Number of unique words:", len(unique_words))
print()
print("Unique words:")
print()
print(unique_words)
