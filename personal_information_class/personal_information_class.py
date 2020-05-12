class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return "Name: " + self.__name + "\nAddress: " + self.__address + "\nAge: " + \
            self.__age + "\nPhone: " + self.__phone_number + "\n"

def main():
    me = PersonalInformation("Max", "123 Main St.", "99", "123-456-7890")
    friend1 = PersonalInformation("Joe", "321 Main St.", "98", "987-654-3210")
    friend2 = PersonalInformation("Sally", "890 Main St.", "100", "456-102-3978")

    print(me)
    print(friend1)
    print(friend2)

main()
