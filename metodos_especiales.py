class Persona: 
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
     
    #define cómo debe representarse un objeto en forma de cadena  
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    #Se utiliza para generar una representación oficial, preferiblemente un string que, cuando se pasa a eval(), recrea el objeto original. 
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    #Este método se invoca cuando utilizas el operador + entre dos objetos.
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + ' '+otro.nombre, nuevo_valor)

# Utiliza __str__ para una representación amigable. 
pers = Persona('Axel', 24)
pers1 = Persona('Nicolas', 12)
print(pers)

# Utiliza __repr__ para una representación oficial.
repre = repr(pers) 
# Evalúa la cadena producida por __repr__ para recrear el objeto.
resultado = eval(repre)
print(repre)
#sumando personas utilizando __add__
new_pers = pers + pers1
print(new_pers)



        