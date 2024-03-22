# Elevar al cubo un número.


def cube():

    # user input
    num = float(input("Enter the number to cube: "))

    # find the cube of the number
    cube = pow(num, 3)
    print(f"\n{num:.2f} cubed is: {cube:.2f}")


if __name__ == "__main__":
    cube()