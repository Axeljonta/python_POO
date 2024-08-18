#El Principio de Inversión de Dependencias (DIP) es el último de 
# los cinco principios SOLID y establece que los módulos de alto 
# nivel no deberían depender de los módulos de bajo nivel. En su lugar,
# ambos deberían depender de abstracciones 
# (interfaces o clases abstractas). Además, las abstracciones no 
# deberían depender de detalles; los detalles deberían depender
# de abstracciones.

# Definimos una interfaz para el almacenamiento
class IAlmacenamiento:
    def guardar(self, datos):
        pass

# Implementamos el almacenamiento en base de datos
class BaseDeDatos(IAlmacenamiento):
    def guardar(self, datos):
        print(f"Guardando {datos} en la base de datos.")

# Implementamos el almacenamiento en archivo
class AlmacenamientoArchivo(IAlmacenamiento):
    def guardar(self, datos):
        print(f"Guardando {datos} en un archivo.")

# Clase Pedido que depende de la abstracción y no de una clase específica
class Pedido:
    def __init__(self, producto, almacenamiento: IAlmacenamiento):
        self.producto = producto
        self.almacenamiento = almacenamiento

    def realizar_pedido(self):
        print(f"Realizando pedido de {self.producto}")
        self.almacenamiento.guardar(self.producto)

# Usamos la clase Pedido con almacenamiento en base de datos
almacenamiento_db = BaseDeDatos()
pedido_db = Pedido("Laptop", almacenamiento_db)
pedido_db.realizar_pedido()

# Usamos la clase Pedido con almacenamiento en archivo
almacenamiento_archivo = AlmacenamientoArchivo()
pedido_archivo = Pedido("Tablet", almacenamiento_archivo)
pedido_archivo.realizar_pedido()
