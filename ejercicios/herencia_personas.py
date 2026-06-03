class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def info(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def info(self):
        super().info()
        print(f"Grado: {self.grado}")

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura
    def info(self):
        super().info()
        print(f"Asignatura: {self.asignatura}")

persona = Persona("Ivan", 25)
estudiante = Estudiante("Juan", 20, "Informatica")
profesor = Profesor("Maria", 30, "Matematicas")

persona.info()
estudiante.info()
profesor.info()
