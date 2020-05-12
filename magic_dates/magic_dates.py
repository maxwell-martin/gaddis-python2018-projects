month = int(input("Enter the month (numeric): "))
day = int(input("Enter the day (numeric): "))
year = int(input("Enter a two digit year: "))

if month * day == year:
    print("The date is magic.")
else:
    print("The date is not magic.")
