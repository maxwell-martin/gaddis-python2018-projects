def cc(msg, shift_amt):
    alphabet = [ "A",
                 "B",
                 "C",
                 "D",
                 "E",
                 "F",
                 "G",
                 "H",
                 "I",
                 "J",
                 "K",
                 "L",
                 "M",
                 "N",
                 "O",
                 "P",
                 "Q",
                 "R",
                 "S",
                 "T", # 19
                 "U", # 20
                 "V", # 21
                 "W", # 22
                 "X", # 23
                 "Y", # 24
                 "Z" ] # 25
    secret = ""

    words = msg.split()

    for word in words:
        for char in word:
            if char not in alphabet:
                secret += "BADCHAR"
            else:
                idx = alphabet.index(char)
                new_idx = idx + shift_amt
                while new_idx > len(alphabet) - 1:
                    new_idx = new_idx - len(alphabet)
                secret += alphabet[new_idx]
        secret += " "

    return secret.strip()

def main():
    message = input("Enter a message: ")
    shift_amount = int(input("Enter a shift amount: "))
    
    secret = cc(message.upper(), shift_amount)

    print(secret)

main()
        
                 
