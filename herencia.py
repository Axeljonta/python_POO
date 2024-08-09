class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def info_persona (self) :
        print(f'\n Empleado: {self.nombre} \n Edad: {self.edad} \n Nacionalidad: {self.nacionalidad}')
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,puesto,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.puesto = puesto
        self.salario = salario
    
    def info_empleado (self) :
        self.info_persona()
        print(f' Puesto: {self.puesto} \n Salario: {self.salario}\n')
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,universidad,carrera):
        super().__init__(nombre,edad,nacionalidad)
        self.universidad = universidad
        self.carrera = carrera
    
    def info_estudiante (self) :
        self.info_persona()
        print(f' Universidad: {self.universidad} \n Carrera: {self.carrera}\n')
        
        

roberto = Empleado('Roberto', 35, 'argentino', 'Programador', 100.000)  
roberto.info_empleado()

matias = Estudiante('Matias', 25,'argentino','UADE', 'Ingenieria en Sistema')
matias.info_estudiante()
