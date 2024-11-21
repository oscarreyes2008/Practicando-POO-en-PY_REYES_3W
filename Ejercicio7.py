class Universidad:
    def __init__(self, nombre):
        self.Nombre = nombre

class Carrera:
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre_universidad, nombre_estudiante, edad_estudiante):
        
        Universidad.__init__(self, nombre_universidad)
        self.nombre = nombre_estudiante
        self.edad = edad_estudiante

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")


persona = Estudiante("Harvard", "Oscar", 19)


persona.carrera("gastronomia")

persona.datos()
