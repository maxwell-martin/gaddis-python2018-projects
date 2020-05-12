pocket_num = int(input("Enter a pocket number: "))

if pocket_num < 0 or pocket_num > 36:
    print("Invalid pocket number.")
else:
    if pocket_num == 0:
        print("Pocket is green.")
    elif pocket_num <= 10 or (pocket_num >= 19 and pocket_num <= 28):
        if pocket_num % 2 != 0:
            print("Pocket is red.")
        else:
            print("Pocket is black.")
    elif (pocket_num >= 11 and pocket_num <= 18) or (pocket_num >= 29 and pocket_num <= 36):
        if pocket_num % 2 != 0:
            print("Pocket is black.")
        else:
            print("Pocket is red.")
