def max(int1, int2):
    if int1 > int2:
        return int1
    elif int1 < int2:
        return int2
    else:
        return 0

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter an integer: "))

greatest_value = max(int1, int2)

if greatest_value != 0:
    print("The largest value is:", greatest_value)
else:
    print("The values are the same.")
