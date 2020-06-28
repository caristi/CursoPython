class Monitor:
    
    contador_monitor = 0
    
    def __init__(self,id_monitor,marca,tamano):
        Monitor.contador_monitor += 1

        self.__id_monitor = Monitor.contador_monitor
        self.__marca = marca
        self.__tamano = tamano
        
        
    def __str__(self):
        return " Monitor id_monitor: " + str(self.__id_monitor) + " Marca: " + self.__marca +" Tamaño: " + self.__tamano
    
    
    def get_id_monitor(self):
        return self.__id_monitor
    
    
    def set_id_monitor(self,id_monitor):
        self.__id_monitor = id_monitor
        
        
    def get_marca(self):
        return self.__marca
    
        
    def set_marca(self,marca):
        self.__marca = marca
        
        
    def get_tamano(self):
        return self.__tamano
    
    
    def set_tamano(self,tamano):
        self.__tamano = tamano
