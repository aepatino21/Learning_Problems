"""
En un puerto se alquilan amarres para barcos de distinto tipo. Para cada ALQUILER se guarda el nombre y CI del cliente,
las fechas inicial y final de alquiler, la posición del amarre y el barco que lo ocupará. 

Un BARCO se caracteriza por su matrícula, su eslora en metros y año de fabricación. 

Un alquiler se calcula multiplicando el número de días de ocupación (incluyendo los días inicial y final) por un módulo función
de cada barco (obtenido simplemente multiplicando por 10 los metros de eslora) y por un valor fijo (1.200 Bs en la actualidad). 

Sin embargo ahora se pretende diferenciar la información de algunos tipos de barcos: número de mástiles para veleros, potencia en CV
para embarcaciones deportivas a motor,  potencia en CV y número de camarotes para yates de lujo.

El módulo de los barcos de un tipo especial se obtiene como el módulo normal más: 
•	El número de mástiles para veleros 
•	La potencia en CV para embarcaciones deportivas a motor 
•	La potencia en CV más el número de camarotes para yates de lujo. 

La App debe permitir ingresar alquilar un barco de cada tipo, mostrar sus datos y el alquiler a pagar por cada uno de ellos. 
"""
from Alquiler import Alquiler
from Barco import Barco
from Puerto import Puerto
from Velero import Velero
from Deportivo import Deportivo
from YateDeLujo import YateDeLujo


def main() -> None:
    # instance of the port
    port = Puerto()

    # adding data to the port
    first_boat = Velero("4564785-1", 25, 1980, 10)
    first_rent = Alquiler("Angel", "30932285", 5, 30, "Puerto A-1", first_boat)
    port.rents.append(first_rent)
    port.boats.append(first_boat)

    # adding another element to the port
    second_boat = Deportivo("8589381-45", 10, 2011, 50)
    second_rent = Alquiler("Julio", "12244594", 2, 12, "Puerto Z-2", second_boat)
    port.rents.append(second_rent)
    port.boats.append(second_boat)
    
    # adding a third element to the port
    third_boat = YateDeLujo("39458390-3", 14, 2021, 40, 7)
    third_rent = Alquiler("Reniher", "12932843", 3, 30, "Puerto C-3", third_boat)
    port.rents.append(third_rent)
    port.boats.append(third_boat)
    
    # show all the available data in the port
    port.show_data()


if __name__ == '__main__':
    main()