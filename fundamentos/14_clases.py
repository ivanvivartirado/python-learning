class Persona:
    
    def __init__(self, nombre, edad, trabajando):
        self.nombre = nombre
        self.edad = edad
        self.trabajando = trabajando
    
    def presentarse(self):
        estado = "estoy trabajando" if self.trabajando else "no estoy trabajando"
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y {estado}."
    
    def cumplir_anos(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."


# Crear una instancia
p = Persona('Ivan', 19, True)

# Usarla
print(p.nombre)        # Ivan
print(p.edad)          # 19
print(p.trabajando)    # True
print(p.presentarse()) # Hola, soy Ivan, tengo 19 años y está trabajando.
print(p.cumplir_anos())
