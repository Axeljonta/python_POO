class CuentaBancaria:
    def __init__(self,saldo,deposito):
        self.__saldo=saldo
        self.__deposito=deposito
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo (self, new_saldo):
        self.__saldo = new_saldo
        
    @saldo.deleter
    def saldo (self):
        del self.__saldo
        
# Crear una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria(120000,0)  

# Obtener el saldo actual
saldo = mi_cuenta.saldo
print(saldo)

# Modificar el saldo usando el setter
mi_cuenta.saldo = 300000
print(mi_cuenta.saldo)

# Eliminando saldo 
del mi_cuenta.saldo 


