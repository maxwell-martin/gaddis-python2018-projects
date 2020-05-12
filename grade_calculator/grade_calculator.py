DISTINCTION = "Distinction"
PASS = "Pass"
CREDIT = "Credit"
FAIL = "Fail"

test1 = int(input("Enter your grade for test one: "))
test2 = int(input("Enter your grade for test two: "))
main_exam = int(input("Enter your grade for the main exam: "))
total_points = test1 + test2 + main_exam

if (test1 < 0 or test1 > 25) or (test2 < 0 or test2 > 25) or \
   (main_exam < 0 or main_exam > 50):
    print("One or more scores entered are invalid.")
else:
    if total_points < 50 or main_exam < 25:
        print("Total points:", total_points, "| Grade:", FAIL)
    elif total_points >= 80:
        print("Total points:", total_points, "| Grade:", DISTINCTION)
    elif total_points >= 60 and total_points < 80:
        print("Total points:", total_points, "| Grade:", CREDIT)
    else:
        print("Total points:", total_points, "| Grade:", PASS)
