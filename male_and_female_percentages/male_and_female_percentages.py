num_males = int(input("Enter the number of males: "))
num_females = int(input("Enter the number of females: "))
total_students = num_males + num_females
percent_males = num_males / total_students
percent_females = num_females / total_students
print("Percentage males:", format(percent_males, ".0%"))
print("Percentage females:", format(percent_females, ".0%"))
