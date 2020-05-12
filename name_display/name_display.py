fn = input("Enter first name: ")
ln = input("Enter last name: ")

initials = fn[0:1].upper() + "." + ln[0:1].upper() + "."
address_book = fn[0:1].upper() + fn[1:].lower() + " " + ln.upper()
username = fn[0:1].lower() + ln.lower()

print("Initials:", initials)
print("Name in address book:", address_book)
print("Username:", username)
