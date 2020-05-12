def num_vowels(s):
    num = 0
    for c in s:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            num += 1
    return num

def num_consonants(s):
    num = 0
    for c in s:
        if c.isalpha():
            if c.lower() not in ["a", "e", "i", "o", "u"]:
                num += 1
    return num

def main():
    string = input("Enter a string: ")
    print("Number of vowels in string:", num_vowels(string))
    print("Number of consonants in string:", num_consonants(string))

main()
        
