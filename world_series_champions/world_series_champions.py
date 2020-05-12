winners = []

with open("WorldSeriesWinners.txt") as infile:
    for line in infile:
        winners.append(line.rstrip("\n"))

choice = input("Enter the name of an MLB team: ")

count = 0
for winner in winners:
    if choice == winner:
        count += 1

print(choice, "has won", count, "times between 1903-2009")
