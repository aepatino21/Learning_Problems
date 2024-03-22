'''
Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante.
La clase Persona tendra los atributos de nombre y edad y un metodo que imprima el nombre y la edad de la persona.
La clase Estudiante heredara de la clase Persona y tambien tendra un atributo adicional: grado y un metodo que imprima el grado del estudiante.

Deberas utilizar super en el metodo de inicializacion (init) para reutilizar el codigo de la clase padre (Persona).
Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funciona correctamente.
'''

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def mostrar_nombre(self):
        print(f"Mi nombre es: {self.nombre}")

    def mostrar_edad(self):
        print(f"Mi edad es: {self.edad}")
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Mi grado es: {self.grado}")


# instancia de la clase Estudiante
primer_estudiante = Estudiante("Angel", 20, "5to")

# prueba de metodos
primer_estudiante.mostrar_nombre()
primer_estudiante.mostrar_edad()
primer_estudiante.mostrar_grado()