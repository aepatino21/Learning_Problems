# Se desea calcular la potencia eléctrica de circuito de la figura 2.6.
# P = V*I y V = R*I.


def electric_power():

    # user input
    current_intensity = float(input("Enter the current intensity: "))
    resistance = float(input("Enter the resistance: "))

    # calculate the volume and power
    voltage = resistance * current_intensity
    power = voltage * current_intensity
    print(f"\nThe power is equal to: {power:.2f}")


if __name__ == "__main__":
    electric_power()