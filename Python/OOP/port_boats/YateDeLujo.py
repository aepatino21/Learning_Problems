from BarcoConMotor import BarcoConMotor

class YateDeLujo(BarcoConMotor):
    def __init__(self, registration_number, length, manufacture_year, motor_hp, total_rooms) -> None:
        super().__init__(registration_number, length, manufacture_year, motor_hp)
        self.__total_rooms = total_rooms

    # getter
    @property
    def total_rooms(self):
        return self.__total_rooms
    
    # setter
    @total_rooms.setter
    def total_rooms(self, new_total_rooms):
        self.__total_rooms = new_total_rooms

    # adding functionality to the calculate_method() method
    def calculate_module(self) -> float:
        return super().calculate_module() + self.motor_hp + self.total_rooms
    
    # redefining __str__
    def __str__(self) -> str:
        return super().__str__() + f"\nCaballos de Fuerza: {self.motor_hp}\nNumero de Camarotes: {self.total_rooms}"