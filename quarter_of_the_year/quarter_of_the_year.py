month = int(input("Enter a month (1-12): "))

if month < 1 or month > 12:
    print("Month not between 1 and 12. Please try again.")
elif month < 4:
    print("The month is in the first quarter.")
elif month > 3 and month < 7:
    print("The month is in the second quarter.")
elif month > 6 and month < 10:
    print("The month is in the third quarter.")
else:
    print("The month is in the fourth quarter.")
