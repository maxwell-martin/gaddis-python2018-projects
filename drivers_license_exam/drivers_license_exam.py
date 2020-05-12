answers = [ "A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]

test_exam = []

with open("random.txt") as infile:
    for line in infile:
        test_exam.append(line.rstrip("\n"))

number_correct = 0
number_incorrect = 0
incorrect_questions = []

index = 0
while index < len(answers):
    if answers[index] == test_exam[index]:
        number_correct += 1
    else:
        number_incorrect += 1
        incorrect_questions.append(index + 1)

    index += 1

status = ""
if number_correct >= 15:
    status = "Passed"
else:
    status = "Failed"

print("Status:", status)
print("Number correct:", number_correct)
print("Number incorrect:", number_incorrect)
print("Questions with incorrect answers:", incorrect_questions)
    
