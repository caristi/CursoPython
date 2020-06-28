class Computadora:
    
    contador_computadoras = 0
    
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        
                
    def __str__(self):
        return ( f""" 
                COMPUTADORA id_computadora: {str(self.__id_computadora)} Nombre: {self.__nombre} 
                {self.__monitor} 
                {self.__teclado}
                {self.__raton}
        """
        )
                