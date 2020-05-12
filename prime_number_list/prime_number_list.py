def is_prime(num):
    divisible_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisible_count += 1
    if divisible_count == 2:
        return True
    else:
        return False

for i in range(2, 100): # 1 is not a prime number by definition, so don't include in list
    if is_prime(i):
        print(i)
