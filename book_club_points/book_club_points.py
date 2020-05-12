books_purchased = int(input("Enter the number of books purchased this month: "))

if books_purchased == 0:
    print("No points awarded.")
elif books_purchased == 2:
    print("5 points awarded.")
elif books_purchased == 4:
    print("15 points awarded.")
elif books_purchased == 6:
    print("30 points awarded.")
elif books_purchased >= 8:
    print("60 points awarded.")
