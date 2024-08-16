def decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar')
        funcion()
        print('Despues de llamar')
    return funcion_modificada

# def saludo():
#     print('Blablabla')

# esta variable seria una funcion
# # saludo_modificado = decorador(saludo)

# lo llamamos como una funcion 
# # saludo_modificado()

#decurador mas estandar
@decorador
def saludo():
    print('Hola Axel ¿estas aprendiendo python?')
    
saludo()
            
#investigar mas de decuradores