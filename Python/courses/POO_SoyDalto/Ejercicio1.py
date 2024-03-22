'''
Crear una clase estudiante que contenga los atributos: Nombre, Edad y Grado
Ademas, debe contener el metodo: estudiar(), el cual imprimira "el estudiante (nombre) esta estudiando"
Importante que el usuario sea quien brinde los datos en plena ejecucion y
finalmente, al escribir "estudiar" (no case sensitive), se ejecutara el metodo estudiar()
'''

# clase para modelar a un estudiante
class Estudiante:
    name = ""
    age = ""
    grade = ""

    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def datos(self) -> None:
        print(f"\n***DATOS DEL ESTUDIANTE***\nNOMBRE: {self.name}\nEDAD: {self.age}\nGRADO: {self.grade}\n")

    def estudiar(self) -> None:
        print(f"el estudiante {self.name} esta estudiando")


# instancia de Estudiante
first_student = Estudiante(input("Nombre: "), input("Edad: "), input("Grado: "))
first_student.datos()
action = input("Si desea que el estudiante se ponga a estudiar, ingrese 'estudiar': ")

if action.lower() == "estudiar":
    first_student.estudiar()