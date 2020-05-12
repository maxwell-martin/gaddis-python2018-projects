# My trivia questions are addition problems.

import question

questions = [
            question.Question("What is 1 + 1?",
                               2,
                               3,
                               4,
                               5, 1),
             question.Question("What is 2 + 2?",
                               1,
                               6,
                               4,
                               -1, 3),
             question.Question("What is 3 + 3?",
                               6,
                               3,
                               4,
                               5, 1),
             question.Question("What is 4 + 4?",
                               9,
                               3,
                               8,
                               2, 3),
             question.Question("What is 5 + 5?",
                               11,
                               12,
                               9,
                               10, 4),
             question.Question("What is 6 + 6?",
                               12,
                               13,
                               14,
                               15, 1),
             question.Question("What is 7 + 7?",
                               12,
                               14,
                               10,
                               13, 2),
             question.Question("What is 8 + 8?",
                               20,
                               18,
                               15,
                               16, 4),
             question.Question("What is 9 + 9?",
                               18,
                               17,
                               21,
                               34, 1),
             question.Question("What is 10 + 10?",
                               13,
                               40,
                               20,
                               30, 3),
        ]

def display_question(i):
    print(questions[i].get_question())
    print("(1) :", questions[i].get_one())
    print("(2) :", questions[i].get_two())
    print("(3) :", questions[i].get_three())
    print("(4) :", questions[i].get_four())

def main():
    p1_points = 0
    print("Player 1, you're up!")
    print()
    for i in range(0,5):
        display_question(i)
        valid_answer = False
        while valid_answer == False:
            try:
                answer = int(input("Enter an answer (1-4): "))
                if answer in range(1,5):
                    valid_answer = True
                    print()
                else:
                    raise Exception
            except:
                print()
                print("Invalid answer. Please enter a number between 1-4.")
                print()
        if answer == questions[i].get_answer():
            p1_points += 1

    print()
    print("--------------------------------------------------")
    print()
                
    p2_points = 0
    print("Player 2, you're up!")
    print()
    for i in range(5,10):
        display_question(i)
        valid_answer = False
        while valid_answer == False:
            try:
                answer = int(input("Enter an answer (1-4): "))
                if answer in range(1,5):
                    valid_answer = True
                    print()
                else:
                    raise Exception
            except:
                print()
                print("Invalid answer. Please enter a number between 1-4.")
                print()
        if answer == questions[i].get_answer():
            p2_points += 1

    print()
    print("--------------------------------------------------")
    print()

    print("Player 1:", p1_points)
    print("Player 2:", p2_points)

    if p1_points > p2_points:
        print("Player 1 wins!")
    elif p1_points < p2_points:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
        
main()
