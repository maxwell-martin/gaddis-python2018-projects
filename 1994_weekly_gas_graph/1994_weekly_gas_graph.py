import matplotlib.pyplot as plt

averages = []

with open("1994_Weekly_Gas_Averages.txt", "r") as infile:
    for line in infile:
        averages.append(float(line.rstrip("\n")))

weeks = []
for i in range(1, 53):
    weeks.append(i)

plt.plot(weeks, averages, marker = "o")

plt.title("Average weekly gas prices for 1994")

plt.xlabel("Week")
plt.ylabel("Average gas price")

plt.grid(True)

plt.show()
