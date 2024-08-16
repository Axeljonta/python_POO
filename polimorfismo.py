class Gato:
    def emitir_sonido(self):
        return "Miau"

class Perro:
    def emitir_sonido(self):
        return "Guau"

# Ejemplo de polimorfismo
def hacer_sonido(animal):
    print(animal.emitir_sonido())

# Creación de objetos
gato = Gato()
perro = Perro()

# Usando polimorfismo
hacer_sonido(gato)  # Output: Miau
hacer_sonido(perro)  # Output: Guau

#Polimorfismo con herencia 

class Gato:
    def emitir_sonido(self):
        return "Miau"

class Perro:
    def emitir_sonido(self):
        return "Guau"

# Ejemplo de polimorfismo
def hacer_sonido(animal):
    print(animal.emitir_sonido())

# Creación de objetos
gato = Gato()
perro = Perro()

# Usando polimorfismo
hacer_sonido(gato)  # Output: Miau
hacer_sonido(perro)  # Output: Guau
 
#esto es otro tipo de polimorfismo ya que le podemos pasa a la misma funcion distintos tipos de datos y funciona igual
def recorrer(var):
    for item in var:
        print(f'Elemento: {item}')
        
var1 = [34, 'hola',[23,'hola']]
var2 = 'Campeon'

print (recorrer(var1), recorrer(var2))
 
 
 
 
 
#Duck typing  
 
#enlaces dinamicos y estaticos 
 
#tipo real tipo declarado