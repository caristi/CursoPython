from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclado = 0
    
    def __init__(self, tipo_entrada, marca,id_teclado):
        super().__init__(tipo_entrada, marca)
        
        Teclado.contador_teclado += 1
        
        self.__id_teclado = Teclado.contador_teclado 
        
        
    def __str__(self):
        return " Teclado id_teclado: " + str(self.__id_teclado) + " "  + super().__str__()    