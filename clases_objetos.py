#como se escriben las clases
#se recomienda usar PascalCase
class Auto ():
    marca = 'Ford'
    modelo = 'Fiesta'
    color = 'Silver'

#como instanciamos una clase (creamos objetos)    
auto1 = Auto()  
marca1 = Auto().marca
#print( f'Su auto es un {marca1} {auto1.modelo}')

#Funcion constructora 
class Celular:
    #toda funcion dentro de una clase se le llama metodo 
    def __init__(self, marca,modelo,camara): 
        self.marca = marca
        self.modelo = modelo
        self.camara = camara 
        
    def llamar(self):
        print(f'Estas haciendo una llamada desde un {self.modelo}...')
        
    def cortar(self):
        print(f'Cortaste la llamada desde tu {self.modelo}...')
        
#Definimos los valores de la clase Celular gracias a la funcion constructora   
celular_samsung = Celular('Samsung','S24','48MP')

celular_samsung.llamar()
print(f'Mi nuevo celular es un {celular_samsung.marca} {celular_samsung.modelo} y tiene una camara de {celular_samsung.camara}.') 
celular_samsung.cortar()

