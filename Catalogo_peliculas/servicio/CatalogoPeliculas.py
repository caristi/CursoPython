import os

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_peliculas(pelicula):
        try:
           archivo = open(CatalogoPeliculas.ruta_archivo,"a")
           archivo.write(pelicula.__str__()+ "\n")
        except Exception as e:
           print("Error al abrir archivo", e)
        finally:
           archivo.close
          
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo,"r")
            print("Catalogo de las Peliculas")
            print(archivo.read())
        except expression as identifier:
            print("Error al listar archivo", e)
        finally:
            archivo.close
            
    @staticmethod
    def eliminar_archivo():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo) 
            print("Archivo eliminado")
        except expression as identifier:
            print("Error al eliminar ")
    
        