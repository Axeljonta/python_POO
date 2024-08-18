from abc import ABC, abstractclassmethod

#esto es una plantilla para crear personas pero no se podria usar la clase directamente 
class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarde(self):
        print(f'Hola, me llamo: {self.nombre} y tengo {self.edad} años')
        
class Estudiente(Persona):
    def __init__(self,nombre,edad,sexo,actividad): 
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f'Estoy estudienado {self.actividad}')
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad): 
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f'Estoy trabajando en el rubro de programacion {self.actividad}')

axel = Estudiente('Axel',24,'Masculino','Programacion') 
tomas = Trabajador('Tomas',26,'Masculino','Programacion') 

axel.hacer_actividad()
tomas.hacer_actividad()


#la abstraccion fomenta el polimorfismo 
