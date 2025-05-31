import datetime
from dataclasses import dataclass
from abc import abstractmethod, ABC

class SchoolClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def lesson_schedule(self):
        pass

class GeoClass(SchoolClass):

    def __init__(self):
        super().__init__()

    def lesson_schedule(self):
        print("1. Country-City game")
        print("2. Main lesson")
        print("3. Homework")

class HistClass(SchoolClass):

    def __init__(self):
        super().__init__()

    def lesson_schedule(self):
        print("1. Exam from previous lesson")
        print("2. Main lesson")


class Scrapper:
    matches_ids = []

    def __init__(self):
        self.hltv_url = "hltv.org"
        self.results_url = "hltv.org/results"

    @staticmethod
    def as_url(url):
        return "https://www." + url

    @classmethod
    def show_matches_ids(cls):
        print(cls.matches_ids)

class VehicleFactory:

    def __init__(self, *, vmax : int, brand : str, wheels : int, color : str, custom : bool):
        self.vmax = vmax
        self.brand = brand
        self.wheels = wheels
        self.color = color
        self.custom = custom

    @classmethod
    def create_porsche(cls):
        return cls(vmax = 300, brand = "porsche", wheels = 4, color = "black", custom = False)

    @classmethod
    def create_opel(cls):
        return cls(vmax = 120, brand = "opel", wheels = 4, color = "purple", custom = True)

    @classmethod
    def create_honda(cls):
        return cls(vmax = 200, brand = "honda", wheels = 4, color = "silver", custom = True)

    def __str__(self):
        return f" vehicle : {self.brand} with vmax {self.vmax} color : {self.color}"


class Country:
    def __init__(self, country : str) -> None:
        self.allowed_countries = ["Poland", "Denmark"]
        self.country = self.validate(country)

    def validate(self, country : str) -> str | None:
        if country not in self.allowed_countries:
            print(f"{country} is not allowed")
            return None
        return country


@dataclass
class Bank:
    name : str
    customers_num : int
    localization : tuple
    country : Country

class BankAccount:

    def __init__(self, *, full_name : str, start_balance, start_time : int, end_time: int) -> None :
        self.__first_name, self.__last_name = full_name.split(" ")
        self.__balance = start_balance
        self.start_time = start_time
        self.end_time = end_time

    @property
    def balance(self) -> None:
        if not self.start_time <= datetime.datetime.now().hour <= self.end_time:
            print("Can not show balance between 7 am and 10 pm")
            return None
        return self.__balance

    @balance.setter
    def balance(self, money : int) -> int | None:
        if money > 1000:
            print("Can not set balance with more than 1000 PLN")
        else:
            self.__balance = money

    def set_full_name(self, full_name : str) -> None:
        if 0 < len(full_name) < 25:
            self.__first_name, self.__last_name = full_name.split(" ")

    def get_full_name(self) -> str:
        return f"{self.__first_name} {self.__last_name}"

    full_name = property(fset = set_full_name, fget = get_full_name)


def main():

    """

    - Instance method - common object method that could be decorated by user custom decorator
    - Static method - logically bond with class but does not involve class or object state
    - Class method - operates on class attributes / construct objects
    - Abstract method - blueprint for inheritance classes

    """

    geo = GeoClass()
    hist = HistClass()
        # calling abstract method with implementation
    hist.lesson_schedule()
    geo.lesson_schedule()
        # calling abstract method of parent class without implementation
    #  Can't instantiate abstract class SchoolClass without an implementation
    # cls = SchoolClass()
    # cls.lesson_schedule()


        # @staticmethod do not involve class(cls) or object(self) attributes
        # its used on object or class and operates only on given arguments
        # performs overall tasks associated with class
    scrapper = Scrapper()
    print(scrapper.as_url("hltv/teams"))
    print(Scrapper.as_url("hltv/results"))

        # @classmethod operates on class attributes - provide cls reference
    Scrapper.show_matches_ids()
    
    
            # @classmethod allows to construct predefined objects using methods
    porsche = VehicleFactory.create_porsche()
    opel = VehicleFactory.create_opel()
    honda = VehicleFactory.create_honda()

    print(porsche)
    print(opel)
    print(honda)
    
    
            # @dataclass provide basic __eq__, __repr__ and __init__ for its object
            # also allows to create own methods
            
    bank1 = Bank("Liberty City Bank", 20500, (100, 100), Country("USA"))
    bank2 = Bank("National State Bank", 5300, (-240, 1400), Country("Denmark"))

    print(bank1)
    print(bank2)

    bank1.name = "City Bank"
    print(bank1)

    print(bank1 == bank2)

    
    acc_551 = BankAccount(full_name = "Jan Kowalski", start_balance=500, start_time=7, end_time=22)

        # setters and getters within API
    print(acc_551.start_time)
    acc_551.start_time = 6
    print(acc_551.start_time)

        # pythonic @decorator
    print(acc_551.balance)
    acc_551.balance = 515
    print(acc_551.balance)

        # pythonic property() notation - attributes exposing, hidden setters and getters implementation
    print(acc_551.full_name)
    acc_551.full_name = "Jagoda Malicka"
    print(acc_551.full_name)


if __name__ == "__main__":
    main()
