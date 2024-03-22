# Hacer un programa que lea una serie de números enteros positivos del teclado y calcule el 
# valor máximo de los mismos y cuántas veces aparece dicho valor repetido. La entrada de datos 
# finalizará cuando se introduzca un 0.


def maximum_number() -> None:
    nums = []
    run_condition = True

    # user input
    while run_condition:
        num = int(input("Enter a positive integer (program closes on 0): "))
        if num == 0:
            run_condition = False
        else:
            if num > 0:
                nums.append(num)
            else:
                print("Error! Negative integers are not supported, try again!")

    maximum = max(nums)
    print(f"\nNumbers = {nums}")
    print(f"\nMaximum number: {maximum}\nOccurrences of maximum number: {nums.count(maximum)}")


if __name__ == "__main__":
    maximum_number()