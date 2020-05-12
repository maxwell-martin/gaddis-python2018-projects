PKG_PRICE = 99.00
TEN_NINETEEN = 0.10
TWENTY_FORTYNINE = 0.20
FIFTY_NINETYNINE = 0.30
ONEHUNDRED_PLUS = 0.40

num_pkgs = int(input("How many software packages did you purchase? "))

discount = 0.0
total = 0.0
subtotal = PKG_PRICE * num_pkgs

if num_pkgs < 10:
    total = subtotal
    print("Discount: $", format(discount, ",.2f"), sep="")
    print("Total: $", format(total, ",.2f"), sep="")
elif num_pkgs >= 10 and num_pkgs <= 19:
    discount = subtotal * TEN_NINETEEN
    total = subtotal - discount
    print("Discount: $", format(discount, ",.2f"), sep="")
    print("Total: $", format(total, ",.2f"), sep="")
elif num_pkgs >= 20 and num_pkgs <= 49:
    discount = subtotal * TWENTY_FORTYNINE
    total = subtotal - discount
    print("Discount: $", format(discount, ",.2f"), sep="")
    print("Total: $", format(total, ",.2f"), sep="")
elif num_pkgs >= 50 and num_pkgs <= 99:
    discount = subtotal * FIFTY_NINETYNINE
    total = subtotal - discount
    print("Discount: $", format(discount, ",.2f"), sep="")
    print("Total: $", format(total, ",.2f"), sep="")
elif num_pkgs >= 100:
    discount = subtotal * ONEHUNDRED_PLUS
    total = subtotal - discount
    print("Discount: $", format(discount, ",.2f"), sep="")
    print("Total: $", format(total, ",.2f"), sep="")
