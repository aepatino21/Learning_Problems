# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

from math import sqrt

# given a number, returns true if prime, false if it's not prime
def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True


def many_primes() -> None:
    primes = []
    enough_primes = False
    counter = 1

    # user input
    num = int(input("Enter the number of primes to print on screen: "))

    # find the num of primes to save it on the primes list
    while enough_primes != True:
        if len(primes) == num:
            enough_primes = True
        else: 
            counter += 1
            if is_prime(counter):
                primes.append(counter)

    print(f"\nFirst {num} primes: {primes}")


if __name__ == "__main__":
    many_primes()