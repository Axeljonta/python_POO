#El Principio de Sustitución de Liskov (LSP) es otro de los 
# principios SOLID que establece que los objetos de una clase 
# derivada deben poder reemplazar a los objetos de la clase base sin alterar el correcto funcionamiento del programa. 
# En otras palabras, las subclases deben ser sustituibles por su 
# clase base sin que esto afecte la correcta ejecución del programa.

class Ave:
    def __init__(self, nombre):
        self.nombre = nombre
        
class AveVoladora(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def volar(self):
        print(f"{self.nombre} está volando.")

class AveNoVoladora(Ave):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # No implementa el método `volar`, ya que no puede volar
    
def hacer_volar(a: Ave):
    if isinstance(a, AveVoladora):
        a.volar()
    else:
        print(f"{a.nombre} no puede volar.")

# Crear instancias de las subclases
aguila = AveVoladora("Aguila")
pinguino = AveNoVoladora("Pingüino")

# Usar la función
hacer_volar(aguila)  
hacer_volar(pinguino)        


