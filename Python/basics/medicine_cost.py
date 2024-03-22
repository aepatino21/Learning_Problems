# Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
# si todos los medicamentos tienen un descuento del 35%.


def medicine_cost():
    DISCOUNT = 0.35

    # user input
    medicine_cost = float(input("Enter the medicine cost: "))

    # calculate the discount and final price
    medicine_discount = medicine_cost * DISCOUNT
    final_price = medicine_cost - medicine_discount
    print(f"\nBrute price: {medicine_cost:.2f}\nDiscount (35%): {medicine_discount:.2f}\nNet price: {final_price:.2f}")


if __name__ == "__main__":
    medicine_cost()