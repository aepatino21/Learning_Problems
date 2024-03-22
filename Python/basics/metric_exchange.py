# Escriba un Algoritmo, que convierta metros a pies y pulgadas (1 metro = 39,37 pulgadas, 1 pie = 12 pulgadas).
# Debe leer la cantidad de metros e imprimirla y su equivalencia en pies y pulgadas


def metric_exchange():
    INCHES = 39.37
    FOOT = 12

    # user input
    meters = float(input("Enter the number of meters: "))

    # calculate in inches and foot
    inch = meters * INCHES
    foot_long = inch / FOOT
    print(f"\nMeters: {meters:.2f}\nInches: {inch:.2f}\nFoot: {foot_long:.2f}")

if __name__ == "__main__":
    metric_exchange()