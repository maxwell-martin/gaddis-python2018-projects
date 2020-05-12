# The instructions for this program are not clear enough.
# RetailItem has a inventory number, but the instructions ignore this.
# Thus, decrementing inventory and checking of inventory levels
# is not dealt with. A better class architecture to handle quantities
# (such as LineItem) would make more sense in this scenario.

import cashregister, retailitem

def main():
    item1 = retailitem.RetailItem("Jelly Beans", 200000, 1.00)
    item2 = retailitem.RetailItem("Snickers", 100000, 1.50)
    item3 = retailitem.RetailItem("York Patties", 300000000, 0.50)
    items = [ item1, item2, item3 ]

    register = cashregister.CashRegister()

    cont = "y"

    while cont == "y":
        print("\n-----------Items available to purchase:---------\n")
        count = 1
        for item in items:
            print("Item (" + str(count) +")")
            print(item)
            count += 1
        try:
            item_choice = int(input("Pick an item to purchase: "))
            if item_choice == 1:
                register.purchase_item(item1)
            elif item_choice == 2:
                register.purchase_item(item2)
            elif item_choice == 3:
                register.purchase_item(item3)
            else:
                raise Exception
        except:
            print("\nInvalid choice. Try again.")
            continue
        cont = input("\nPurchase more items (y/n)? ").lower()

    print("\n-----------Items selected to purchase:---------\n")
    register.show_items()

    print("Total is: $" + format(register.get_total(), ",.2f"))
    
main()
