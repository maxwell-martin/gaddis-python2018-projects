total = 0;

for day in range(5):
    num_collected = int(input("Enter the number of bugs collected for day " + str(day + 1) + ": "))
    total += num_collected

print("Total bugs collected over 5 days:", total)
