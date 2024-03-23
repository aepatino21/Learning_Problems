from Barco import Barco

class Velero(Barco):
    def __init__(self, registration_number, length, manufacture_year, ship_mast_num) -> None:
        super().__init__(registration_number, length, manufacture_year)
        self.__ship_mast_num = ship_mast_num

    # getter
    @property
    def ship_mast_num(self):
        return self.__ship_mast_num
    
    # setter
    @ship_mast_num.setter
    def ship_mast_num(self, new_ship_mast_num):
        self.__ship_mast_num = new_ship_mast_num

    # adding new functionality to the calculate_module() method
    def calculate_module(self) -> float:
        return super().calculate_module() + self.ship_mast_num
    
    # redefining __str__
    def __str__(self) -> str:
        return super().__str__() + f"\nNumero de Mastiles: {self.ship_mast_num}"