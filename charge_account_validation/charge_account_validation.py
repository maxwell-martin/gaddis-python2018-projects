accts = []

with open("charge_accounts.txt", "r") as infile:
    for line in infile:
        accts.append(line.rstrip("\n"))

acct = input("Enter an account number: ")

if acct in accts:
    print("Number is valid.")
else:
    print("Number is invalid.")
