#  En un hospital existen tres áreas. El presupuesto anual del hospital se reparte conforme a la siguiente tabla:  
# Área / Porcentaje del presupuesto
# Ginecología  40% 
# Traumatología  30% 
# Pediatría  30% 
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestario.


def hospital_budget():

    #user input
    total_budget = float(input("Enter this year's budget: "))

    # calculate the percentage of the budget for each area of the hospital
    gynecology = total_budget * 0.40
    traumatologies = total_budget * 0.30
    pediatric = traumatologies
    print(f"\nYear's Budget: {total_budget:.2f}\nGynecology: {gynecology:.2f} (40%)\nTraumatologies: {traumatologies:.2f} (30%)\nPediatric: {pediatric:.2f} (30%)")


if __name__ == "__main__":
    hospital_budget()