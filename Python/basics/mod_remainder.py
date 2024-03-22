# Leer dos números enteros y realizar un Algoritmo,que determine el cociente entero y su resto.
# El primer número es el dividendo y el segundo es el divisor


def mod_remainder():

    # user input
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    # find the mod and remainder
    remainder = int(first_number / second_number)
    mod = first_number % second_number
    print(f"\nRemainder: {remainder}\nMod: {mod:.2f}")


if __name__ == "__main__":
    mod_remainder()