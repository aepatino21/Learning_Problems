# Un  profesor  desea  saber  qué  porcentaje  de  hombres  y  que  porcentaje  de  mujeres  hay  en  un  grupo  de  
# estudiantes.


def men_women():
    men = int(input("Enter the number of men: "))
    women = int(input("Enter the number of women: "))

    # calculate the total of students
    total_students = men + women

    # calculate the percentage of men and women
    men_percentage = (men * 100) / total_students
    women_percentage = (women * 100) / total_students

    print(f"In a classroom of {total_students} students, there's a percentage of {men_percentage:.2f} men and {women_percentage:.2f} women.")


if __name__ == "__main__":
    men_women()