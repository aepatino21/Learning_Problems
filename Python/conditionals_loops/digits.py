# Dado un número entero determine la cantidad de dígitos que tiene


def digits() -> None:
    
    # user inputs
    num = int(input("Enter the number to find out how many digits it has: "))

    # find out how many digits the number has
    digits = len(str(num))
    print(f"\nThe number has {digits} digits")


if __name__ == "__main__":
    digits()