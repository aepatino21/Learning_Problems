# Diseñar un Algoritmo, que realice la siguiente conversión: lea una temperatura en grados Celsius (C) la
# lleve a grados Fahrenheit (F) y viceversa. Nota: la formula de conversión es: F = (9/5) C + 32


def temperature_exchange():

    # menu
    menu = int(input("What temperature system will be used? (0 = Celsius, 1 = Fahrenheit) "))
    temperature = float(input("Enter the temperature data: "))
    if menu == 0:
        # Celsius
        final_temperature = ((9/5) * temperature) + 32
    else:
        # Fahrenheit
        final_temperature = (temperature - 32) * (5/9)

    print(f"\nThe temperature in the other system is: {final_temperature:.2f}")


if __name__ == "__main__":
    temperature_exchange()