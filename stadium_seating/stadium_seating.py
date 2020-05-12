CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

a = int(input("Enter number of class A seats sold: "))
b = int(input("Enter number of class B seats sold: "))
c = int(input("Enter number of class C seats sold: "))

income_a = a * CLASS_A
income_b = b * CLASS_B
income_c = c * CLASS_C

print("Income generated from class A: $", format(income_a, ",.2f"), sep="")
print("Income generated from class B: $", format(income_b, ",.2f"), sep="")
print("Income generated from class C: $", format(income_c, ",.2f"), sep="")
