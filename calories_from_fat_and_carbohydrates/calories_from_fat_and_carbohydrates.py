fat_grams = float(input("Enter fat grams consumed today: "))
calories_from_fat = fat_grams * 9

carb_grams = float(input("Enter carb grams consumed today: "))
calories_from_carbs = carb_grams * 4

print("Calories from fat: ", format(calories_from_fat, ".2f"))
print("Calories from carbs: ", format(calories_from_carbs, ".2f"))
