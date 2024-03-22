# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber 
# cuánto  dinero  obtendrá  por  concepto  de  comisiones  por  las  tres  ventas  que  realiza  en  el  mes  y  el  total  que  
# recibirá en el mes tomando en cuenta su sueldo base y comisiones.


def salesman_salary():
    BASE_SALARY = 1200

    # user input
    first_sale = float(input("Enter the total of the first sale: "))
    second_sale = float(input("Enter the total of the second sale: "))
    third_sale = float(input("Enter the total of the third sale: "))

    commission = (first_sale + second_sale + third_sale) * 0.1
    net_salary = BASE_SALARY + commission
    print(f"\nBrute salary: {BASE_SALARY:.2f} \nSales commission: 10% ({commission:.2f}) \nNet Salary: {net_salary:.2f}")


if __name__ == "__main__":
    salesman_salary()