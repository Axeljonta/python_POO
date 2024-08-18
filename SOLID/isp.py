#El Principio de Segregación de Interfaces (ISP) es uno de los 
# principios SOLID que establece que una interfaz no debería obligar 
# a las clases a depender de métodos que no utilizan. 
# En otras palabras, las interfaces deben ser específicas para el 
# cliente que las usa y no deben incluir métodos que no son 
# relevantes para algunas de las clases que las implementan.

# Interfaces específicas para cada funcionalidad
class IImpresora:
    def imprimir(self):
        pass

class IEscaner:
    def escanear(self):
        pass

class IFotocopiadora:
    def fotocopiar(self):
        pass

# Implementación de una impresora que solo puede imprimir
class Impresora(IImpresora):
    def imprimir(self):
        print("Imprimiendo documento.")

# Implementación de un escáner
class Escaner(IEscaner):
    def escanear(self):
        print("Escaneando documento.")

# Implementación de una fotocopiadora
class Fotocopiadora(IFotocopiadora):
    def fotocopiar(self):
        print("Fotocopiando documento.")
        
impresora = Impresora()
impresora.imprimir()  # Salida: Imprimiendo documento.

escaner = Escaner()
escaner.escanear()   # Salida: Escaneando documento.

fotocopiadora = Fotocopiadora()
fotocopiadora.fotocopiar()  # Salida: Fotocopiando documento.

