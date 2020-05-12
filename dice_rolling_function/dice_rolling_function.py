import random

def roll(number_of_throws):
    lst = []
    
    for i in range(number_of_throws):
        lst.append(random.randint(1, 6))

    lst.sort()

    return lst

def main():
    num = int(input("Enter a positive integer: "))
    lst = roll(num)
    print(lst)

main()
