# Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.


def product_table() -> None:

    # user input
    num = int(input("Enter the number to find its product table: "))

    # create the product table
    for i in range(0, 11):
        print(f"{num} x {i} = {num * i}")


if __name__ == "__main__":
    product_table()