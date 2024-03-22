# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá 
# pagar finalmente por su compra.


def shop_discount():
    DISCOUNT = 0.15

    # user input
    total = float(input("Enter your purchase total: "))
    total -= (total * DISCOUNT)

    print(f"The total with the applied discount (15%) is: {total:.2f}")


if __name__ == "__main__":
    shop_discount()