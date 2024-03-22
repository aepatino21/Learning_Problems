# Realizar un algoritmo que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible
# entre él mismo y la unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número

from math import sqrt

def is_prime() -> None:
    prime = True

    # user input
    num = int(input("Enter the number to find out if it's a prime number: "))

    # find out whether is a prime number or not
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    print(f"\nIs {num} a prime number? The answer is {prime}")


if __name__ == "__main__":
    is_prime()