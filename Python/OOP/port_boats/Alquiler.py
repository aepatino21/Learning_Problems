from Barco import Barco

class Alquiler:
    def __init__(self, name, id, initial_date, final_date, position, boat: Barco) -> None:
        self.__name = name
        self.__id = id
        self.__initial_date = initial_date
        self.__final_date = final_date
        self.__position = position
        self.__boat = boat

    # getters
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def initial_date(self):
        return self.__initial_date
    
    @property
    def final_date(self):
        return self.__final_date
    
    @property
    def position(self):
        return self.__position
    
    @property
    def boat(self):
        return self.__boat
    
    # setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @initial_date.setter
    def initial_date(self, new_initial_date):
        self.__initial_date = new_initial_date

    @final_date.setter
    def final_date(self, new_final_date):
        self.__final_date = new_final_date

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    @boat.setter
    def boat(self, new_boat):
        self.__boat = new_boat

    # method to calculate the total rent
    def calculate_rent(self) -> float:
        occupation_days = self.final_date - self.initial_date
        total_rent = occupation_days * 1200 * self.boat.calculate_module()
        return total_rent
    
    # redefining __str__
    def __str__(self) -> str:
        data = f"\n***DATOS DE LA FACTURA***\nNombre: {self.name}\nID: {self.id} \nFecha Inicial: {self.initial_date}\nFecha Final: {self.final_date}\nPosicion de Amarre: {self.position}\nTotal a Pagar: {self.calculate_rent()} Bs."
        return data