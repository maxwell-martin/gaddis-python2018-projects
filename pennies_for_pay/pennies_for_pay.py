days = int(input("Enter the number of days: "))

salary = 0.00
total = 0.00

print("Day\tSalary")
print("---------------")

for day in range(1, days + 1):
    if day == 1:
        salary = 0.01
    else:
        salary *= 2

    total += salary

    print(day, "\t$", format(salary, ",.2f"))

print("---------------")
print("Total pay: $", format(total, ",.2f"), end="")
