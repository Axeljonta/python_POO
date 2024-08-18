#La idea principal detrás del SRP es que si una clase tiene más de 
# una responsabilidad, esos diferentes aspectos de la clase tienden
# a estar acoplados entre sí. Si uno de esos aspectos cambia, puede 
# afectar a otros, lo que conduce a código menos mantenible y más 
# propenso a errores. El SRP busca hacer que las clases sean más simples 
# y enfocadas en una única tarea, lo que facilita la comprensión, el 
# mantenimiento y la evolución del código.
# Violación del principio SRP
# class Reporte:
#     def __init__(self, datos):
#         self.datos = datos

#     def generar_reporte(self):
#         # Lógica para generar el reporte
#         return f"Reporte con datos: {self.datos}"

#     def imprimir_reporte(self):
#         # Lógica para imprimir el reporte
#         print(self.generar_reporte())

# # Esta clase tiene dos responsabilidades: generar y manejar el reporte.

# Cumple el principio SRP
class GeneradorDeReporte:
    def __init__(self, datos):
        self.datos = datos

    def generar(self):
        # Lógica para generar el reporte
        return f"Reporte con datos: {self.datos}"

class ImpresoraDeReporte:
    def imprimir(self, reporte):
        # Lógica para imprimir el reporte
        print(reporte)

# Uso:
datos = {"ventas": 1000, "gastos": 500}
generador = GeneradorDeReporte(datos)
reporte = generador.generar()

impresora = ImpresoraDeReporte()
impresora.imprimir(reporte)

