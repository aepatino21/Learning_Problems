# En un estacionamiento cobran $/. 1.500 por hora o fracción. 
# Diseñe un algoritmo que determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, 
# conociendo el tiempo de estacionamiento en horas y minutos


def parking_cost():
    COST = 1.500

    # user input
    hours = int(input("Enter the number of hours the vehicle was in the parking lot: "))
    minutes = int(input("Enter the number of minutes the vehicle was in the parking lot: "))

    # calculate the total cost of parking
    total_cost = (hours * COST) + (((minutes * 1) / 60) * COST)
    print(f'The total cost is: {total_cost:.2f}')
    

if __name__ == "__main__":
    parking_cost()