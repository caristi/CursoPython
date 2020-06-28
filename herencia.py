class Vehiculo:
    """DocString de la clase vehiculo"""
    
    def __init__(self,color, cantidad_ruedas):
        self.color           = color
        self.cantidad_ruedas = cantidad_ruedas
        
    def __str__(self):
        return "color " + self.color + " y la cantidad de ruedas es " + str(self.cantidad_ruedas) + "."

class Coche(Vehiculo):
    
    def __init__(self, color, cantidad_ruedas,velocidad):
        super().__init__(color, cantidad_ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return "El coche es "+ super().__str__() + " Ademas la velocidad es " + str(self.velocidad)
    
class Bicicleta(Vehiculo): 
    
    def __init__(self, color, cantidad_ruedas,tipo):
        super().__init__(color, cantidad_ruedas)  
        self.tipo = tipo
        
    def __str__(self):
        return "La bicicleta es " + super().__str__() + " Ademas el tipo es " + self.tipo    

vehiculo = Vehiculo("Rojo",4)

coche = Coche("Vinotinto",4,10)
print(coche)

bicicleta = Bicicleta("Negra",2,"Montaña")
print(bicicleta)

print(help(vehiculo))