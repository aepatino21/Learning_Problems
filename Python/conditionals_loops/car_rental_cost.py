# Una compañía dedicada al alquiler de automóviles cobra un monto fijo de $300.000 para los primeros 300 km de recorrido.
# Para más de 300 km y hasta 1000 km, cobra un monto adicional de $ 15.000 por cada kilómetro en exceso sobre 300.
# Para más de 1000 km cobra un monto adicional de $ 10.000 por cada kilómetro en exceso sobre 1000. Los precios
# ya incluyen el 20% del impuesto general a las ventas, IVA. Diseñe un algoritmo que determine el monto a pagar por el alquiler de un vehículo y el monto incluido del impuesto.


def car_rental_cost() -> None:
    COST = 300000
    IVA = 0.20

    # user input
    km = float(input("Enter the number of driven Km: "))
    aux = km

    # calculate the total cost
    if km <= 300:
        total_cost = COST
    else:
        if km > 300 and km <= 1000:
            total_cost = 15000 * (km - 300) + COST
        else:
            total_cost = 15000 * 700 + 10000 * (km - 1000) + COST

    paid_tax = total_cost * IVA
    print(f"Car rental cost: {total_cost:.2f}\nPaid Tax (20%): {paid_tax:.2f}")


if __name__ == "__main__":
    car_rental_cost()