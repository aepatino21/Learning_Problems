# Realizar un algoritmo que pida un número y calcule su factorial
# (El factorial de un número es el producto de todos los enteros
# entre 1 y el propio número y se representa
# por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).


def factorial() -> None:
    fact = 1

    # user input
    num = int(input("Enter the number to find its factorial form: "))

    if num < 0:
        print(f"Number must be greater than 0!")
    else:
        if num == 1 or num == 0:
            print(f"Factorial: {fact}")
        else:
            for i in range(1, num + 1):
                fact *= i

            print(f"Factorial: {fact}")


if __name__ == "__main__":
    factorial()