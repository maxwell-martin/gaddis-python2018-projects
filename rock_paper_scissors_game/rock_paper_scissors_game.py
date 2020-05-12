import random

def main():
    display_welcome()
    wants_to_play = "y"
    while wants_to_play == "y":
        wants_to_play = play()

def play():
    computer_choice = generate_computer_choice()
    user_choice = get_user_choice()
    print("Computer Choice:", computer_choice)
    print("------------------------------------------------------")
    results = get_winner(user_choice, computer_choice)
    if results == "Tie":
        print("It's a tie! The game must be played again to determine winner.")
        return "y"
    else:
        print(results, "won!")
        print("------------------------------------------------------")
        return input("Play again (y/n)? ")

def get_user_choice():
    display_instructions()
    choice = input("User Choice: ")
    while not is_valid_choice(choice):
        print("Invalid choice. Please try again.")
        display_instructions()
        choice = input("User Choice: ")
    return choice

def display_instructions():
    print("------------------------------------------------------")
    print("Type one of the following:")
    print("rock")
    print("paper")
    print("scissors")
    print("------------------------------------------------------")

def display_welcome():
    print("Welcome to the Rock, Paper, Scissors game.")

def is_valid_choice(choice):
    if choice == "rock" or choice == "paper" or choice == "scissors":
        return True
    else:
        return False

def generate_computer_choice():
    num_choice = random.randint(1, 3)
    if num_choice == 1:
        return "rock"
    elif num_choice == 2:
        return "paper"
    else:
        return "scissors"

def get_winner(user_choice, computer_choice):
    if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
                    (user_choice == "paper" and computer_choice == "rock"):
        return "User"
    elif user_choice == computer_choice:
        return "Tie"
    else:
        return "Computer"

main()
