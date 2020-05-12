winner_counts = {}
winner_years = {}

with open("WorldSeriesWinners.txt", "r") as infile:
    year = 1903

    for line in infile:
        
        line = line.rstrip("\n")
        
        if line in winner_counts:
            winner_counts[line] += 1
        else:
            winner_counts[line] = 1

        if year == 1904 or year == 1994:
            winner_years[year] = "No World Series was played that year."
        else:
            winner_years[year] = line

        year += 1

year = int(input("Enter a year between 1903 and 2009 (inclusive): "))

while year < 1903 or year > 2009:
    year = int(input("Invalid year. Enter a year between 1903 and 2009 (inclusive): "))

print()

if year == 1904 or year == 1994:
    print(winner_years[year])
else:
    winner = winner_years[year]
    number_of_wins = winner_counts[winner]

    print("In", str(year) + ", the", winner, "won the World Series.")
    print("The", winner, "have won the World Series", number_of_wins, "times.")





        
