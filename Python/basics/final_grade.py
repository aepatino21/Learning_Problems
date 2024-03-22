# Un alumno desea saber cuál será su calificación final en la asignatura: Introducción a la informática. Dicha 
# calificación se compone de los siguientes porcentajes:  
#  55% del promedio de sus tres calificaciones parciales.  
#  30% de la calificación del examen final.  
#  15% de la calificación de un trabajo final.


def final_grade():
    first_exam = float(input("Enter the first exam grade: "))
    second_exam = float(input("Enter the second exam grade: "))
    third_exam = float(input("Enter the third exam grade: "))
    final_exam = float(input("Enter the final exam grade: "))
    final_work = float(input("Enter the final work grade: "))

    # Calculate the final grade with all the previous grades
    final_grade = ((((first_exam + second_exam + third_exam)/3) * 0.55) + (final_exam * 0.30) + (final_work * 0.15))
    print(f"The final grade is: {final_grade:.2f}")


if __name__ == "__main__":
    final_grade() 