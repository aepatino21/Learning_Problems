# Diseñe un algoritmo que lea tres longitudes y determine si forman o no un triángulo.
# Si es un triángulo determine de qué tipo de triángulo se trata entre: equilátero (si tiene tres lados iguales),
# isósceles (si tiene dos lados iguales) o escaleno (si tiene tres lados desiguales).
# Considere que para formar un triángulo se requiere que: "el lado mayor sea menor que la suma de los otros dos lados"


def insert_length(lengths: list) -> None:
    length = float(input("Enter a length: "))
    lengths.append(length)


def determine_triangle() -> None:
    lengths = []

    # user input
    insert_length(lengths)
    insert_length(lengths)
    insert_length(lengths)
    
    # find max length
    max_length = max(lengths)
    lengths.remove(max_length)

    # determine if it's a triangle and in case that it's one, find its type
    if max_length < sum(lengths):
        if max_length == lengths[0] and max_length == lengths[1] and lengths[0] == lengths[1]:
            print("It is an equilateral triangle (3 equal lengths)")
        elif max_length == lengths[0] or max_length == lengths[1] or lengths[0] == lengths[1]:
            print("It is an isosceles triangle! (2 equal lengths)")
        else:
            print("It is an scalene triangle! (0 equal lengths)")
    else:   
        print(f"It is not a triangle!")


if __name__ == "__main__":
    determine_triangle()