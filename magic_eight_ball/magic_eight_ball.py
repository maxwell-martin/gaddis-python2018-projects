import random

responses = []

with open("8_ball_responses.txt", "r") as infile:
    for line in infile:
        responses.append(line.rstrip("\n"))

again = "y"

while again.lower() == "y":
    question = input("Ask a question: ")
    print(responses[random.randint(0, len(responses) - 1)])
    again = input("Again (y/n)? ")
