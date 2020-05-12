import pickle

def main():
    choice = 0
    menu = get_menu()
    while choice != 4:
        show_menu(menu)
        
        print()
        
        show_options()
        
        print()
        
        try:
            choice = int(input("What would you like to do? "))
        except:
            print()
            print("----------------------- INVALID CHOICE. PLEASE TRY AGAIN. -----------------------")
            continue
        
        if choice == 1:
            menu = add_vegetable(menu)
        elif choice == 2:
            menu = change_price(menu)
        elif choice == 3:
            menu = delete_vegetable(menu)
        elif choice != 4:
            print()
            print("----------------------- INVALID CHOICE. PLEASE TRY AGAIN. -----------------------")

    serialize(menu)
        

def show_menu(menu):
    print()
    print("Pickled Vegetables Menu:")
    print("----------------------------------------------")

    if len(menu) == 0:
        print("- No vegetables on the menu.")
    else:
        for key, value in menu.items():
            print("-", key, ": " + "$" + format(value, ",.2f"))
    print("----------------------------------------------")

def show_options():
    print("Options:")
    print("----------------------------------------------")
    print("- (1) Add a new vegetable")
    print("- (2) Change price of existing vegetable")
    print("- (3) Delete a vegetable")
    print("- (4) Exit")
    print("----------------------------------------------")

def get_menu():
    try:
        menu_file = open("menu.dat", "rb")
        menu = pickle.load(menu_file)
        menu_file.close()
        return menu
    except:
        # Default menu when menu.dat doesn't exist or has not data in it
        return { "Broccoli" : 3.00, "Lettuce" : 2.00, "Carrots" : 1.00 }

def add_vegetable(menu):
    print()
    vegetable = input("What is the name of the vegetable? ")

    valid_price = False

    while valid_price == False:
        try:
            price = float(input("Enter price of vegetable: "))
            if price > 0:
                if vegetable not in menu:
                    menu[vegetable] = price
                else:
                    print()
                    print("-----------------------", vegetable, "already exists. -----------------------")
            else:
                print()
                print("----------------------- Invalid price. Please try again. -----------------------")
                print()
                continue
            return menu
        except:
            print()
            print("----------------------- Invalid price. Please try again. -----------------------")
            print()
        
def change_price(menu):
    print()
    vegetable = input("What is the name of the vegetable? ")

    if vegetable in menu:
        valid_price = False

        while valid_price == False:
            try:
                price = float(input("Enter new price of vegetable: "))
                if price > 0:
                    menu[vegetable] = price
                else:
                    print()
                    print("----------------------- Invalid price. Please try again. -----------------------")
                    print()
                    continue
                return menu
            except:
                print()
                print("----------------------- Invalid price. Please try again. -----------------------")
                print()
    else:
        print()
        print("-----------------------", vegetable, "not listed on the menu. -----------------------")
        return menu
        
def delete_vegetable(menu):
    print()
    vegetable = input("What is the name of the vegetable? ")

    if vegetable not in menu:
        print()
        print("-----------------------", vegetable, "not listed on the menu. -----------------------")
        return menu
    else:
        menu.pop(vegetable)
        return menu
        
def serialize(menu):
    try:
        menu_file = open("menu.dat", "wb")
        pickle.dump(menu, menu_file)
        menu_file.close()
    except IOError as err:
        print("Error saving menu to file:")
        print(err)

main()
