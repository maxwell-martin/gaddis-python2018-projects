BURN_RATE = 4.2

print("Calories burned:")
print("----------------")

for time in range(10, 31, 5):
    calories_burned = BURN_RATE * time
    print("After", str(time),
          "minutes:",
          str(format(calories_burned, ".2f")),
          "calories.")
