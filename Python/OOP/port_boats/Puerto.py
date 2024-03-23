from Alquiler import Alquiler
from Barco import Barco

class Puerto:
    def __init__(self) -> None:
        self.__rents = []
        self.__boats = []

    # method to show rents and boats' data
    def show_data(self) -> None:
        for i in range(0, len(self.__rents)):
            print(f"\nAlquiler numero: {i + 1}")
            print(self.__rents[i])
            print(self.__boats[i])

    # getters
    @property
    def rents(self) -> list:
        return self.__rents
    
    @property
    def boats(self) -> list:
        return self.__boats
    
    # setters
    @rents.setter
    def rents(self, index, rent: Alquiler) -> None:
        self.__rents[index] = rent

    @boats.setter
    def boats(self, index, boat: Barco) -> None:
        self.__boats[index] = boat