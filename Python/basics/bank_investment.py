# Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganara después 
# de un mes si el banco paga a razón de 2% mensual.


def bank_investment():
    RATE = 0.02
    capital = float(input("Enter the amount of money to invest: "))
    interest = capital * RATE
    print(f"The interest earned in a month is {interest:.2f}")
    

if __name__ == "__main__":
    bank_investment()