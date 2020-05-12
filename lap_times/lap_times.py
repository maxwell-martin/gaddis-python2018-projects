laps = int(input("How many laps did you do? "))

fastest_lap_time = 0.0
slowest_lap_time = 0.0
total_lap_times = 0.0

for lap in range(1, laps + 1):
    time = float(input("Enter time in seconds for lap " + str(lap) + ": "))

    total_lap_times += time
    
    if time > slowest_lap_time:
        slowest_lap_time = time

    if time < fastest_lap_time or fastest_lap_time == 0.0:
        fastest_lap_time = time

print("Fastest lap time:", str(fastest_lap_time))
print("Slowest lap time:", str(slowest_lap_time))

average_lap_time = total_lap_times / laps

print("Average lap time:", str(average_lap_time))
