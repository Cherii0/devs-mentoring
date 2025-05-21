

class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__field = 0
        self.__circuit = 0


    def calculate_circuit(self):

        self.__circuit = ( self.__length * 2 ) + ( self.__width * 2 )

    def calculate_field(self):

        self.__field = self.__length * self.__width


    def get_field(self):
        return self.__field

    def get_circuit(self):
        return self.__circuit

    def get_len_width(self):
        return self.__length, self.__width

def main():

    rec1 = Rectangle(2, 4)
    rec1.calculate_circuit()
    rec1.calculate_field()

    print(f"obwod prostokata o parametrach {rec1.get_len_width()} wynosi {rec1.get_circuit()}")
    print(f"pole prostokata o parametrach {rec1.get_len_width()} wynosi { rec1.get_field()}")

if __name__ == "__main__":
    main()
