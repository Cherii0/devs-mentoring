

class Vehicle:
    def __init__(self, type_vehicle, mileage, max_speed):
        self.__type_vehicle = type_vehicle
        self.__mileage = mileage
        self.__max_speed = max_speed

    def __str__(self):
        return self.__type_vehicle

    def get_mileage(self):
        return self.__mileage

    def update_mileage(self, mileage):
        print(f"{self.__type_vehicle} have travelled {mileage} kilometers")
        if mileage >= 0:
            self.__mileage += mileage


def main():

    car = Vehicle("car", 300000, 200)
    kilometers = 100

    print(f"{car} have {car.get_mileage()} kilometers mileage")
    car.update_mileage(kilometers)
    print(f"{car} have {car.get_mileage()} kilometers mileage")



if __name__ == '__main__':
    main()
