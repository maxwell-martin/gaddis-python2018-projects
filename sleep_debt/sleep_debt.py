DESIRED_SLEEP_HRS = 8.00

total_sleep_hours = 0.00

for day in range(1, 8):
    hours = float(input("Enter the number of hours slept for day " + str(day) + ": "))
    total_sleep_hours += hours

sleep_debt = (DESIRED_SLEEP_HRS * 7) - total_sleep_hours

print("Sleep debt:", format(sleep_debt, ".0f"), "hour(s)")

if sleep_debt <= 0:
    print("I am jealous that you do not have sleep debt.")
