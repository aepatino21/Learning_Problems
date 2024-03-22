# Elaborar un Algoritmo, que calcule el IVA a un monto leído y lo imprima por pantalla


def iva_calculator():
    IVA = 0.16

    # user input
    price = float(input("Enter the price without IVA: "))

    # calculate the IVA
    final_price = price + (price * IVA)
    print(f"\nThe price with IVA (16%) is: {final_price:.2f}")


if __name__ == "__main__":
    iva_calculator()