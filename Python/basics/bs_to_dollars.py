# Dada una cantidad en bolívares, obtener la equivalencia en dólares, asumiendo que la unidad cambiaría es un 
# dato desconocido.


def bs_to_dollars():
    dollars = float(input("Enter the rate of change (Bs. -> $): "))
    bs = float(input("Enter the amount of Bs.: "))
    print(f"{bs:.2f} Bs. are {(bs/dollars):.2f} dollars.")


if __name__ == "__main__":
    bs_to_dollars()