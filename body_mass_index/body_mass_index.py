height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in pounds: "))

bmi = weight * 703 / height ** 2

print("BMI:", format(bmi, ".2f"))

if bmi >= 18.5 and bmi <= 25:
    print("Optimal weight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Overweight")
