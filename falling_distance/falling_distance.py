def falling_distance(falling_time_seconds):
    return 0.5 * 9.8 * falling_time_seconds ** 2

print("Falling Time\tFalling Distance")
print("------------------------------")

for i in range(1, 11):
    print(i, "\t\t", format(falling_distance(i), ".2f"))
