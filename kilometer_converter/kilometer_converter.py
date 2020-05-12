CONVERSION_AMT = 0.6214

def main():
    km = get_user_input()
    miles = calculate_miles(km)
    print("Amount in miles is: " + format(miles, ".2f"))

def get_user_input():
    km = float(input("Enter distance in kilometers: "))
    return km

def calculate_miles(km):
    return km * CONVERSION_AMT

main()
