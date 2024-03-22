# Diseñe un algoritmo que lea los datos necesarios y calcule la masa,  según la formula siguiente
# mass = (pressure * volume)/(0.37 * (temperature + 460))


def mass_formula():
    
    # user input
    pressure = float(input("Enter the pressure: "))
    volume = float(input("Enter the volume: "))
    temperature = float(input("Enter the temperature: "))

    # calculate the mass
    mass = (pressure * volume) / (0.37 * (temperature + 460))
    print(f"The mass is: {mass:.2f}")


if __name__ == "__main__":
    mass_formula()