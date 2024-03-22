# Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. 
# Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera



def route_average():

    # user input
    monday_time = float(input("How long did it take (in minutes) to complete the route on monday: "))
    wednesday_time = float(input("How long did it take (in minutes) to complete the route on wednesday: "))
    friday_time = float(input("How long did it take (in minutes) to complete the route on friday: "))

    # calculate the average time
    time_sum = monday_time + wednesday_time + friday_time
    average_time = time_sum / 3
    print(f"The average time required to complete the route is {average_time:.2f} minutes.")


if __name__ == "__main__":
    route_average()