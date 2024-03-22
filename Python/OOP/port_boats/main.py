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


def main() -> None:
    pass


if __name__ == '__main__':
    main()