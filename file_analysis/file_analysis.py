words1 = set()
words2 = set()

with open("words1.txt", "r") as infile1:
    for line in infile1:
        words1.add(line.rstrip("\n"))

with open("words2.txt", "r") as infile2:
    for line in infile2:
        words2.add(line.rstrip("\n"))

print(len(words1))
print(len(words2))

# All unique words contained in both files
unique_words_all = words1.union(words2)
print()
print(unique_words_all)

# All words that appear in both files
words_both_files = words1.intersection(words2)
print()
print(words_both_files)

# All words that appear in file1 but not file2
words_file1_only = words1.difference(words2)
print()
print(words_file1_only)

# All words that appear in file2 but not file1
words_file2_only = words2.difference(words1)
print()
print(words_file2_only)

# All words that appear in either file1 or file2 but not both
words_either_file_only = words1.symmetric_difference(words2)
print()
print(words_either_file_only)

