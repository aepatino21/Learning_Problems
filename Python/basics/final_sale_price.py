# El dueño de una tienda compra un artículo a un precio determinado.
# Obtener el precio en que lo debe vender para obtener una ganancia del 30%.


def final_sale_price():
    PROFIT = 0.30

    # user input
    price = float(input("Enter the price of the product: "))

    # calculate the required price to obtain profits of 30%
    final_price = price + (price * PROFIT)
    print(f"\nTo obtain a profit of 30%, the item needs to be sold for: ${final_price:.2f}")


if __name__ == "__main__":
    final_sale_price()