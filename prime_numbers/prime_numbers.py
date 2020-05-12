def is_prime(num):
    divisible_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisible_count += 1
    if divisible_count == 2:
        return True
    else:
        return False

num = int(input("Enter a natural number greater than 1: "))

while num < 2:
    print("Incorrect value.")
    num = int(input("Enter a natural number greater than 1: "))

if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
