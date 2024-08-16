#ejemplo basico de encapsulamiento
class MiClase: 
    def __init__(self,privado): 
        self.__atributo_privado = 'valor' #no se puede acceder al atributo
        self._privado = privado #esto es una convecion que se usa para que otros desarrolladores entiendan que es un dato privado
    def __hablar(self): #metodo privado 
        print('Estoy hablando') 
        
#getters y setters
class CuentaBancaria:
    def __init__(self,saldo,deposito):
        self.__saldo=saldo
        self.__deposito=deposito
    
    #para obtener el dato
    def get_saldo(self):
        return self.__saldo
    
    #para modificar un dato privado 
    def set_deposito(self, new_deposito):
        self.__deposito = new_deposito 
        self.__saldo += self.__deposito
        return self.__saldo
        

mi_cuenta = CuentaBancaria(120000,0)  

saldo = mi_cuenta.get_saldo()
print(saldo)

deposito = mi_cuenta.set_deposito(20000)
print(deposito)