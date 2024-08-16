# Definimos la clase abstracta Auto
class Auto(ABC):
    def __init__(self):
        self._estado = 'apagado'
        
    def encender(self):
        self._estado = 'encendido'
        print('El auto esta encendido')
    
    def conducir(self):
        if self._estado == 'apagado':
            self.encender()
        print("El auto está en movimiento.")
        
mi_auto = Auto()
mi_auto.conducir()