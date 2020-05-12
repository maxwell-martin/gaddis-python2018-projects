codes = {'a': "!",
         'b': "@",
         'c': "$",
         'd': "%",
         'e': "^",
         'f': "&",
         'g': "*",
         'h': "(",
         'i': ")",
         'j': "_",
         'k': "+",
         'l': "1",
         'm': "2",
         'n': "3",
         'o': "4",
         'p': "5",
         'q': "6",
         'r': "7",
         's': "8",
         't': "9",
         'u': "0",
         'v': "-",
         'w': "=",
         'x': "~",
         'y': "`",
         'z': "[",
         'A': "]",
         'B': "\\",
         'C': "{",
         'D': "}",
         'E': "|",
         'F': ";",
         'G': "'",
         'H': ":",
         'I': '"',
         'J': ",",
         'K': ".",
         'L': "/",
         'M': "<",
         'N': ">",
         'O': "?",
         'P': "µ",
         'Q': "¢",
         'R': "¤",
         'S': "¥",
         'T': "¦",
         'U': "§",
         'V': "«",
         'W': "»",
         'X': "¿",
         'Y': "Ø",
         'Z': "þ",
         ' ': "ö",
         '\n':"\n"}

# Encryption
with open("decrypted_message.txt", "r") as infile:
    with open("encrypted_message.txt", "w") as outfile:
        for line in infile:
            #line = line.rstrip("\n")
            encrypted_line = ""
            for char in line:
                encrypted_line += codes[char]
            outfile.write(encrypted_line)
            
# Decryption
with open("encrypted_message.txt", "r") as infile:
    for line in infile:
        line = line.rstrip("\n")
        decrypted_line = ""
        for char in line:
            for key, value in codes.items():
                if char == value:
                    decrypted_line += key
        print(decrypted_line)
