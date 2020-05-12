import random

play = "y"
while play == "y" or play == "Y":
    random_number = random.randint(1, 100)
    game_over = False
    count = 0
    while not game_over:
        user_number = int(input("Enter a number between 1 and 100: "))
        count += 1
        if user_number > random_number:
            print("Too high, try again.")
        elif user_number < random_number:
            print("Too low, try again.")
        else:
            print("Congratulations! It took you", count, "tries to guess correctly.")
            game_over = True
            play = input("Type \"y\" to play again or any key to exit: ")
