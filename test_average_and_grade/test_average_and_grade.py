def calc_average(t1, t2, t3, t4, t5):
    return (t1 + t2 + t3 + t4 + t5) / 5

def determine_grade(grade):
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    elif grade >= 0 and grade <= 59:
        return "F"
    else:
        return "Invalid grade"

t1 = float(input("Enter test score 1: "))
t2 = float(input("Enter test score 2: "))
t3 = float(input("Enter test score 3: "))
t4 = float(input("Enter test score 4: "))
t5 = float(input("Enter test score 5: "))

print("Score\tLetter Grade")
print("-------------------")

print(t1, "\t\t", determine_grade(t1))
print(t2, "\t\t", determine_grade(t2))
print(t3, "\t\t", determine_grade(t3))
print(t4, "\t\t", determine_grade(t4))
print(t5, "\t\t", determine_grade(t5))

print("Average test score:", format(calc_average(t1, t2, t3, t4, t5), ".2f"))
