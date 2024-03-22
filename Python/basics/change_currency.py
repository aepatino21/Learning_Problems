# Calcular el cambio de monedas en dólares y euros al ingresar cierta cantidad en Bs.
# (tipo de cambio $= 2,150Bs, Euros: 1,45 $).


def change_currency():
    DOLLAR = 2150
    EURO = 1.45

    # user input
    bs = float(input("Enter the amount of Bs.: "))

    # calculate with a currency exchange
    dollars = bs / DOLLAR
    euros = dollars / EURO
    print(f"\nBs.: {bs:.2f}\nDollars: {dollars:.2f}\nEuros: {euros:.2f}")


if __name__ == "__main__":
    change_currency()