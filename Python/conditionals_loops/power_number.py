# Realizar un algoritmo que dados dos números, uno real (base) y un entero positivo (exponente),
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.


def power_number() -> None:

    # user input
    base = float(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    # find the power of the number
    num_power = base
    for i in range(1, exponent):
        num_power *= base

    print(f"{base} to the power of {exponent} = {num_power}") 


if __name__ == "__main__":
    power_number()