# Un alumno desea saber cuál será su promedio general en las tres materias más difíciles que cursa y cuál será el
# promedio que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación:
# La calificación de Matemáticas se obtiene de la sig. Manera:
#  Examen 90%
#  Promedio de tareas 10%
#  En esta materia se pidió un total de tres tareas.
# La calificación de Física se obtiene de la sig. Manera:
#  Examen 80%
#  Promedio de tareas 20%
#  En esta materia se pidió un total de dos tareas.
# La calificación de Química se obtiene de la sig. Manera:
#  Examen 85%
#  Promedio de tareas 15%
#  En esta materia se pidió un promedio de tres tareas.


def math():
    
    # user input
    test = float(input("Enter your grade on the math test: "))
    first_homework = float(input("Enter your grade on the first math homework: "))
    second_homework = float(input("Enter your grade on the second math homework: "))
    third_homework = float(input("Enter your grade on the third math homework: "))

    final_math_grade = (test * 90)/20 + ((first_homework + second_homework + third_homework) * 10)/60
    return final_math_grade / 5


def physics():
    
    # user input
    test = float(input("Enter your grade on the physics test: "))
    first_homework = float(input("Enter your grade on the first physics homework: "))
    second_homework = float(input("Enter your grade on the second physics homework: "))

    final_physics_grade = (test * 80)/20 + ((first_homework + second_homework) * 20)/40
    return final_physics_grade / 5


def chemistry():
    
    # user input
    test = float(input("Enter your grade on the chemistry test: "))
    first_homework = float(input("Enter your grade on the first chemistry homework: "))
    second_homework = float(input("Enter your grade on the second chemistry homework: "))
    third_homework = float(input("Enter your grade on the third chemistry homework: "))

    final_chemistry_grade = (test * 85)/20 + ((first_homework + second_homework + third_homework) * 15)/60
    return final_chemistry_grade / 5


def final_grade_hardest():

    # find the grade on the classes
    math_grade = math()
    physics_grade = physics()
    chemistry_grade = chemistry()

    # calculate the average of the three classes
    average_grade = (math_grade + physics_grade + chemistry_grade) / 3
    print(f"\nThe average between the three hardest classes is: {average_grade:.2f}" +
          f"\nMath grade: {math_grade:.2f}\nPhysics grade: {physics_grade:.2f}\nChemistry grade: {chemistry_grade:.2f}")


if __name__ == "__main__":
    final_grade_hardest()