from abc import ABC
from Barco import Barco

class BarcoConMotor(ABC, Barco):
    def __init__(self, registration_number, length, manufacture_year, motor_hp) -> None:
        super().__init__(registration_number, length, manufacture_year)
        self._motor_hp = motor_hp

    # getter
    @property
    def motor_hp(self):
        return self._motor_hp
    
    # setter
    @motor_hp.setter
    def motor_hp(self, new_motor_hp):
        self._motor_hp = new_motor_hp
