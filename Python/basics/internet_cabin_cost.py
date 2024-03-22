# Calcular el monto a pagar en una cabina de Internet si el costo por hora es de Bs/.1,5 
# y por cada 5 horas te dan una hora de promoción gratis.

from math import floor

def internet_cabin_cost():

    RATE = 1.5

    # user input
    hours = int(input("How many hours were you in the cabin? "))
    total = None

    # calculate the total with any applied discount
    if hours < 5:
        total = hours * RATE
    else:
        discount = floor(hours / 5) * RATE
        total = (hours * RATE) - discount

    print(f"\nThe total to pay is: {total:.2f} Bs.")


if __name__ == "__main__":
    internet_cabin_cost()