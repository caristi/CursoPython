class Orden:
    
    contador_ordenes = 0
    
    def __init__(self,computadoras):
        Orden.contador_ordenes = Orden.contador_ordenes + 1
        
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = computadoras
        
        
    def __str__(self):
        computadoras_str = ""
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()
        
        return " Orden id_orden: " + str(self.__id_orden) + " " + computadoras_str
    
    
    def agregarComputadora(self,computadora):        
        self.__computadoras.append(computadora)