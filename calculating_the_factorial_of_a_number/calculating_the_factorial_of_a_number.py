factorial_number = int(input("Enter a nonnegative integer: "))

result = 1

while factorial_number < 0:
    factorial_number = int(input("Enter a nonnegative integer: "))

if factorial_number == 0:
    print(factorial_number, "! is equal to ", result, sep="")
else:
    for i in range(1, factorial_number + 1):
        result *= i

    print(factorial_number, "! is equal to ", result, sep="")
        
