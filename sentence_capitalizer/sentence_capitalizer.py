sentences = input("Enter one or more sentences with no capitalizaton: ")

new_sentences = ""

char_index = 0
sentence_start_index = 0

for char in sentences:
    if char == "." or char == "!" or char == "?":
        sentence = sentences[sentence_start_index:char_index + 1].strip()
        sentence_start_index = char_index + 1

        first_letter = sentence[0:1].upper()
        the_rest = sentence[1:]

        if sentences[char_index + 1:char_index + 2] in ["!", ".", "?"]:
            combo = first_letter + the_rest
        else:
            combo = first_letter + the_rest + " "
        
        new_sentences += combo

    char_index += 1

print(new_sentences)
