class RetailItem:
    def __init__(self, item_description, units_in_inventory, price):
        self.__item_description = item_description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    def set_item_description(self, item_description):
        self.__item_description = item_description

    def set_units_in_inventory(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return "Item Description: " + self.__item_description + \
            "\nUnits in Inventory: " + str(self.__units_in_inventory) + \
            "\nPrice: $" + format(self.__price, ",.2f") + "\n"
