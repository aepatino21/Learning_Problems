# Elaborar un Algoritmo, que intercambie los valores de dos variables numéricas.
# Ejemplo:    Datos de entrada: X=3;    Y=9.       La respuesta será: X=9, Y=3    


def swap():

    # user input
    x = float(input("Enter the first number (x): "))
    y = float(input("Enter the second number (y): "))

    # swap
    y,x = x,y
    print(f"\nSwap:\nx = {x:.2f}\ny = {y:.2f}")


if __name__ == "__main__":
    swap()