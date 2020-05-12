num_int = int(input("Enter an integer: "))

if num_int > 0:
    print("Positive")
elif num_int < 0:
    print("Negative")
else:
    print("Zero")

if num_int % 2 == 0:
    print("Even")
else:
    print("Odd")
