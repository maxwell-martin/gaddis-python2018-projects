year = int(input("Enter a four digit year (YYYY): "))

if year % 100 == 0:
    if year % 400 == 0:
        print("In ", year, ", February has 29 days.", sep="")
    else:
        print("In ", year, ", February has 28 days.", sep="")
else:
    if year % 4 == 0:
        print("In ", year, ", February has 29 days.", sep="")
    else:
        print("In ", year, ", February has 28 days.", sep="")
