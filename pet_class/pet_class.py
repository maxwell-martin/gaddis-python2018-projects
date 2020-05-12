class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name = input("Enter the pet's name: ")
    animal_type = input("Enter the pet's animal type: ")
    age = int(input("Enter the pet's age: "))

    pet = Pet(name, animal_type, age)

    print("Your pet's name:", pet.get_name())
    print("Your pet's animal type:", pet.get_animal_type())
    print("Your pet's age:", pet.get_age())

main()
