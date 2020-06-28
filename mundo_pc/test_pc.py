from Orden import Orden
from Computadora import Computadora
from Raton  import Raton
from Teclado import Teclado
from Monitor import Monitor

raton = Raton("USB","Genius","222")
teclado = Teclado("USB","Asus","1235454")
monitor = Monitor("HDMI","Samsung","99999")
computadora = Computadora("Trabajo",monitor,teclado,raton)

computadoras = [computadora]
orden = Orden(computadoras)
print(orden)

raton2 = Raton("USB","Genius 2","231")
teclado2 = Teclado("USB","Asus 5","313134")
monitor2 = Monitor("HDMI","Samsung","99999")
computadora2 = Computadora("MAC",monitor2,teclado2,raton2)
orden.agregarComputadora(computadora2)
print(orden)
