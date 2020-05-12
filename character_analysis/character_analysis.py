with open("text.txt") as infile:
    num_up = 0
    num_low = 0
    num_dig = 0
    num_whit = 0

    for line in infile:
        for char in line:
            if char.isupper():
                num_up += 1
            if char.islower():
                num_low += 1
            if char.isdigit():
                num_dig += 1
            if char.isspace():
                num_whit += 1

print("Number of uppercase letters:", num_up)
print("Number of lowercase letters:", num_low)
print("Number of digits:", num_dig)
print("Number of whitespace characters:", num_whit)
