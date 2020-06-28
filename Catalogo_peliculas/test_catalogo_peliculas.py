from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    print("Opciones:")
    print("1. Agregar peliculas: ")
    print("2. Listar peliculas: ")
    print("3. Eliminar archivo")
    print("4. Salir")
    
    opcion = int(input("Agregar la opción que se desea: "))
    if opcion == 1:
       nombre_pelicula = input("Cuál es el nombre de la pelicula: ")
       pelicula = Pelicula(nombre_pelicula)
       CatalogoPeliculas.agregar_peliculas(pelicula)
    elif opcion == 2:
        CatalogoPeliculas.listar_peliculas()
    elif opcion == 3:
        CatalogoPeliculas.eliminar_archivo()    
else:
    print("Salimos del programa")