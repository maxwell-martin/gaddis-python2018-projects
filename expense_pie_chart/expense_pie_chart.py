import matplotlib.pyplot as plt

expenses = []

with open("expenses.txt", "r") as infile:
    for line in infile:
        expenses.append(line.rstrip("\n"))

slice_labels = ["Rent", "Gas", "Food", "Clothing", "Car payment", "Misc"]

plt.pie(expenses, labels = slice_labels)

plt.title("Expenses for last month")

plt.show()
