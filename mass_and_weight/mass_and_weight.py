mass_kg = float(input("Enter the object's weight in kilograms: "))
weight_N = mass_kg * 9.8

if weight_N > 500.0:
    print("The object is too heavy.")
elif weight_N < 100.0:
    print("The object is too light.")
else:
    print("The object is in the weight range.")
