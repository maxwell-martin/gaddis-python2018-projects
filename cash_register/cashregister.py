class CashRegister:
    def __init__(self):
        self.__items = []

    def purchase_item(self, item):
        self.__items.append(item)

    def get_total(self):
        total = 0
        for item in self.__items:
            total += item.get_price()
        return total

    def show_items(self):
        for item in self.__items:
            print(item)

    def clear(self):
        self.__items = []
