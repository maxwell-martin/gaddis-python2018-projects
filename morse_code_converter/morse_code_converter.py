codes = { ",":"--.--",
          ".":".-.-.-",
          "?":"..--..",
          "0":"-----",
          "1":".----",
          "2":"..---",
          "3":"...--",
          "4":"....-",
          "5":".....",
          "6":"-....",
          "7":"--...",
          "8":"---..",
          "9":"----.",
          "A":".-",
          "B":"-...",
          "C":"-.-.",
          "D":"-..",
          "E":".",
          "F":"..-.",
          "G":"--.",
          "H":"....",
          "I":"..",
          "J":".---",
          "K":"-.-",
          "L":".-..",
          "M":"--",
          "N":"-.",
          "O":"---",
          "P":".--.",
          "Q":"--.-",
          "R":".-.",
          "S":"...",
          "T":"-",
          "U":"..-",
          "V":"...-",
          "W":".--",
          "X":"-..-",
          "Y":"-.-",
          "Z":"--.." }

message = input("Enter a message: ")

message = message.strip()

if message != "":
    morse_msg = ""
    group = message.split(" ")
    for word in group:
        for char in word:
            if char.isalpha():
                morse_msg += codes[char.upper()]
            elif char not in codes.keys():
                morse_msg += "BADCHAR"
            else:
                morse_msg += codes[char]
        morse_msg += " "
    print(morse_msg.strip())
else:
    print("Invalid input.")
        
