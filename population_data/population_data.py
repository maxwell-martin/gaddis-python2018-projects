population = []

with open("USPopulation.txt", "r") as infile:
    for line in infile:
        population.append(int(line.rstrip("\n")))

changes = []

index = 0

total = 0
while index < len(population) - 1:
    pop_change = population[index + 1] - population[index]
    total += pop_change
    changes.append(pop_change)
    index += 1

average = total // len(changes)

print("Average annual change in population:", average)
print("Year with greatest increase in population:", changes.index(max(changes)) + 1950)
print("Year with smallest increase in population:", changes.index(min(changes)) + 1950)
