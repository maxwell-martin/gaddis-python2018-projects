speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

print("Hour\tDistance Traveled")
print("-------------------------")

for hour in range(hours):
    distance = speed * (hour + 1)
    print(str(hour + 1), "\t\t", str(distance))
