# Ignores whitespace chars
def mfc(s):
    chars = {}
    for c in s:
        if not c.isspace():
            if c in chars.keys():
                chars[c] += 1
            else:
                chars[c] = 1
    print(chars)
    max_count_char = 0
    max_count_key = ""
    for key in chars.keys():
        if chars[key] > max_count_char:
            max_count_char = chars[key]
            max_count_key = key
    return max_count_key

def main():
    string = input("Enter a string: ")
    print("Most frequent character:", mfc(string))

main()
