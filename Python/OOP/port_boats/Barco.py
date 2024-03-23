class Barco:
    def __init__(self, registration_number, length, manufacture_year) -> None:
        self._registration_number = registration_number
        self._length = length
        self._manufacture_year = manufacture_year

    # getters
    @property
    def registration_number(self):
        return self._registration_number
    
    @property
    def length(self):
        return self._length
    
    @property
    def manufacture_year(self):
        return self._manufacture_year
    
    # setters
    @registration_number.setter
    def registration_number(self, new_registration_number):
        self._registration_number = new_registration_number

    @length.setter
    def length(self, new_length):
        self._length = new_length

    @manufacture_year.setter
    def manufacture_year(self, new_manufacture_year):
        self._manufacture_year = new_manufacture_year

    # method to calculate the module of the boat (used to determine the total rent)
    def calculate_module(self) -> float:
        return 10 * self.length
    
    # redefining __str__
    def __str__(self) -> str:
        return f"\n***DATOS DEL BARCO***\nNum. Placa: {self.registration_number}\nEslora (metros): {self.length}\nManufacture Date: {self.manufacture_year}"