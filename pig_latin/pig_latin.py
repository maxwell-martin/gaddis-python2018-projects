def convert_to_pig_latin(sentence):
    words = sentence.upper().split()
    pig_latin_sentence = ""
    for word in words:
        if len(word) > 1:
            first_letter = word[0:1]
            the_rest = word[1:]
            pl = the_rest + first_letter + "AY "
        else:
            pl = word + "AY "
        pig_latin_sentence += pl
    return pig_latin_sentence.strip()

def main():
    sentence = input("Enter a sentence without punctuation: ")
    pls = convert_to_pig_latin(sentence)
    print("English:\t", sentence)
    print("Pig Latin:\t", pls)

main()
