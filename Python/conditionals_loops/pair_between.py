# Realizar un algoritmo que imprima todos los números pares entre dos números
# que se le pidan al usuario. 


def pair_between() -> None:
    pairs = []

    # user input
    start = int(input("Enter the first number (start): "))
    end = int(input("Enter the second number (end): "))

    # find all pair numbers between start and end
    for i in range(start + 1, end):
        if i % 2 == 0:
            pairs.append(i)

    print(f"Pair numbers between {start} and {end}: {pairs}")


if __name__ == "__main__":
    pair_between()