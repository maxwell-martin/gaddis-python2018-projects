class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    car = Car(2020, "Toyota")

    for i in range(5):
        car.accelerate()
        print("Current speed: ", car.get_speed())

    for i in range(5):
        car.brake()
        print("Current speed: ", car.get_speed())

main()
