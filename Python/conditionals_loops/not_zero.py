# Realizar un algoritmo que pida números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos


def not_zero():
    nums = []
    is_zero = False

    while is_zero != True:

        # user input
        num = float(input("Enter the next num (program will stop once a zero is found): "))
        if num != 0:
            nums.append(num)
            continue
        is_zero = True

    print(f"\nThe nums were: {nums}")
    print(f"\nThe sum of all the numbers is: {sum(nums):.2f}\nThe average of the numbers is: {(sum(nums)/len(nums)):.2f}")


if __name__ == "__main__":
    not_zero()