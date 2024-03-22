# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su salario actual
# y un descuento de 2,5% por servicios.


def new_salary():
    RAISE = 0.08
    SERVICES = 0.025

    # user input
    salary = float(input("Enter your current salary: "))

    # calculate the new salary
    new_salary = salary + (salary * RAISE)
    new_salary -= new_salary * SERVICES
    print(f"\nThe new salary is: {new_salary:.2f}")


if __name__ == "__main__":
    new_salary()