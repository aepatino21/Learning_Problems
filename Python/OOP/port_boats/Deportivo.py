from BarcoConMotor import BarcoConMotor

class Deportivo(BarcoConMotor):
    def __init__(self, registration_number, length, manufacture_year, motor_hp) -> None:
        super().__init__(registration_number, length, manufacture_year, motor_hp)

    # redefine the calculate_module() method
    def calculate_module(self) -> float:
        return super().calculate_module() + self.motor_hp
    
    # redefine __str__
    def __str__(self) -> str:
        return super().__str__() + f"\nCaballos de Fuerza: {self.motor_hp}"