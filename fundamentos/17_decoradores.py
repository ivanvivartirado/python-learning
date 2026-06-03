# DECORADORES EN PYTHON
# Los decoradores modifican el comportamiento de funciones o métodos

# @property — convierte un método en atributo y permite validaciones

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # _ indica que es "privado" por convención
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print("La edad no puede ser negativa")
        else:
            self._edad = nueva_edad

persona = Persona("Ivan", 19)
print(persona.nombre)  # accedes como atributo, no como método()
print(persona.edad)

persona.edad = 20      # usa el setter automáticamente
print(persona.edad)

persona.edad = -5      # validación salta
print(persona.edad)    # sigue siendo 20
class Calculadora:
    
    # @staticmethod — método que no necesita acceder a la clase ni a la instancia
    # No recibe self ni cls — es como una función normal pero dentro de la clase
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

    # @classmethod — método que recibe la clase como primer argumento (cls)
    # Se usa para crear instancias de formas alternativas
    @classmethod
    def desde_string(cls, operacion: str):
        # operacion = "5+3"
        partes = operacion.split("+")
        return cls.sumar(int(partes[0]), int(partes[1]))

# Usar staticmethod sin crear instancia
print(Calculadora.sumar(5, 3))       # 8
print(Calculadora.es_par(4))         # True
print(Calculadora.es_par(7))         # False

# Usar classmethod
print(Calculadora.desde_string("5+3"))  # 8