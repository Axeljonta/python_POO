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