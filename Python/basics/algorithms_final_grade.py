# Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de tres exámenes parciales.


def algorithms_final_grade():

    # user input
    first_grade = float(input("Enter the grade of the first test (Min: 0 & Max: 20): "))
    second_grade = float(input("Enter the grade of the second test (Min: 0 & Max: 20): "))
    third_grade = float(input("Enter the grade of the third test (Min: 0 & Max: 20): "))

    # calculate the final grade of algorithms
    final_grade = ((first_grade + second_grade + third_grade) * 20) / 60
    print(f"\nYour final grade is: {final_grade:.2f} pts.")


if __name__ == "__main__":
    algorithms_final_grade()