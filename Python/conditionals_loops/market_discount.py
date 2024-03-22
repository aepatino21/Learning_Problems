# Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 docenas 
# y 10% en caso contrario. Además por la compra de más de 3 docenas
# se obsequia una unidad del producto por cada docena en exceso sobre 3. Diseñe un algoritmo que determine el monto de la compra,
# el monto del descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto.


def market_discount():
    BIG_DISCOUNT = 0.15
    SMALL_DISCOUNT = 0.10
    given_units = 0

    # user input
    product_cost = float(input("Enter the cost of the dozen: "))
    dozens = int(input("Enter the amount of dozens that will be bought: "))

    # calculate the cost and discount of the dozens
    if dozens <= 3:
        product_discount = (dozens * product_cost) * SMALL_DISCOUNT
        brute_cost = (dozens * product_cost) - product_discount
    else:
        given_units = dozens - 3
        product_discount = (dozens * product_cost) * BIG_DISCOUNT
        brute_cost = (dozens * product_cost) - product_discount

    print(f"\nProduct cost: {product_cost:.2f}\nDozens bought: {dozens}\nGiven Units: {given_units}")
    print(f"Brute total: {dozens * product_cost:.2f}\nTax: {product_discount:.2f}\nTotal: {brute_cost:.2f}")


if __name__ == "__main__":
    market_discount()