def main():
    file = open("steps.txt", "r")
    month = 1
    while month <= 12:
        average = get_average_monthly_steps(month, file)
        display_average_monthly_steps(month, average)
        month += 1

def get_average_monthly_steps(month, file):
    monthly_total = 0
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        for i in range(31):
            monthly_total += int(file.readline())
        return monthly_total / 31
    elif month == 2:
        for i in range(28):
            monthly_total += int(file.readline())
        return monthly_total / 28
    else:
        for i in range(30):
            monthly_total += int(file.readline())
        return monthly_total / 30

def display_average_monthly_steps(month, average_monthly_steps):
    if month == 1:
        print("January :", format(average_monthly_steps, ",.0f"))
    elif month == 2:
        print("February :", format(average_monthly_steps, ",.0f"))
    elif month == 3:
        print("March :", format(average_monthly_steps, ",.0f"))
    elif month == 4:
        print("April :", format(average_monthly_steps, ",.0f"))
    elif month == 5:
        print("May :", format(average_monthly_steps, ",.0f"))
    elif month == 6:
        print("June :", format(average_monthly_steps, ",.0f"))
    elif month == 7:
        print("July :", format(average_monthly_steps, ",.0f"))
    elif month == 8:
        print("August :", format(average_monthly_steps, ",.0f"))
    elif month == 9:
        print("September :", format(average_monthly_steps, ",.0f"))
    elif month == 10:
        print("October :", format(average_monthly_steps, ",.0f"))
    elif month == 11:
        print("November :", format(average_monthly_steps, ",.0f"))
    elif month == 12:
        print("December :", format(average_monthly_steps, ",.0f"))

main()

### TEST
##file = open("test.txt", "r")
##
##total = 0
##
##for line in file:
##    total += int(line)
##
##average = total / 28
##
##print(average)
