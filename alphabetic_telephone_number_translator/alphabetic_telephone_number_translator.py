numbers = { "A":2,
            "B":2,
            "C":2,
            "D":3,
            "E":3,
            "F":3,
            "G":4,
            "H":4,
            "I":4,
            "J":5,
            "K":5,
            "L":5,
            "M":6,
            "N":6,
            "O":6,
            "P":7,
            "Q":7,
            "R":7,
            "S":7,
            "T":8,
            "U":8,
            "V":8,
            "W":9,
            "X":9,
            "Y":9,
            "Z":9 }

number = input("Enter a 10 digit phone number (XXX-XXX-XXXX): ")

group = number.split("-")

new_number = ""

for word in group:
    for char in word:
        if char.isalpha():
            new_number += str(numbers[char.upper()])
        else:
            new_number += char
    new_number += "-"

print(new_number.rstrip("-"))          
