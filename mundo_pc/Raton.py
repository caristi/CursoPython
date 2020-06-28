from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contador_raton = 0
    
    def __init__(self,tipo_entrada,marca,id_raton):                   
        Raton.contador_raton += 1
        
        self.__id_raton = Raton.contador_raton
        self._tipo_entrada = tipo_entrada
        self._marca = marca
        
        
    def __str__(self):
        return " Raton: id_Raton: " + str(self.__id_raton) + " Tipo Entrada :" + self._tipo_entrada + " Marca: " + self._marca 
