class Persona: 
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def info_persona (self) :
        print(f'\n Empleado: {self.nombre} \n Edad: {self.edad} \n Nacionalidad: {self.nacionalidad}')
        
class Estudiante:
    def __init__(self,universidad,carrera):
        self.universidad = universidad
        self.carrera = carrera
        
    def info_estudiante (self) :
        print(f' Universidad: {self.universidad} \n Carrera: {self.carrera}')
        
class EstudianteEmpleado(Persona,Estudiante):
    def __init__(self, nombre, edad, nacionalidad, universidad, carrera, empresa, puesto):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Estudiante.__init__(self,universidad,carrera)
        self.empresa = empresa
        self.puesto = puesto
        
    def info_estudiante_empleado(self):
        Persona.info_persona(self)  
        Estudiante.info_estudiante(self)  
        print(f' Empresa: {self.empresa} \n Puesto: {self.puesto}\n')
        
roberto = EstudianteEmpleado('Roberto', 35, 'argentino', 'UADE', 'Ingenieria en Sistema' ,'Google', 'Programador')  
roberto.info_estudiante_empleado()

#devuelve True si la clase EstudianteEmpleado es una subclase de Estudiante 
herencia = issubclass(EstudianteEmpleado,Estudiante)

#devuelve True si la instacia roberto es una instancia de Estudiante 
instancia = isinstance(roberto,Estudiante)

print (herencia, instancia)

print(EstudianteEmpleado.mro())

      