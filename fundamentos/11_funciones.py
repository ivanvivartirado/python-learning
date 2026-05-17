def f(x):
    return 2*x
y = f(3)
print (y) #6



def di_hola():
    print("Hola")

di_hola()

# Ahora pasaremos como entrada un nombre imprimiremos hola y el nombre

def hola_nombre(nombre):
    print("Hola", nombre)
hola_nombre("Ivan")

# Argumentos por posicion

def resta (a, b):
    return a-b
print(resta(5, 3)) # Resultado 2

# Argumentos por defecto

def suma (a, b, c=20):
    return a+b+c
print (suma (5, 5)) # Dado que el parámetro c tiene un valor por defecto, la función puede ser llamada sin ese valor.

# Asignar valor por defecto a todos los parametros

def sumapred(a=3, b=5, c=0):
    return a+b+c
print (sumapred()) # Resultado 8 

# Argumentos de longitud variable

def sumavar (numeros):
    total = 0
    for n in numeros:
        total += n
    return total
print(sumavar([1, 3, 5, 4]))

# Sentencia return 
# El uso de la sentencia return permite realizar dos cosas:
# Salir de la función y transferir la ejecución de vuelta a donde se realizó la llamada.
# Devolver uno o varios parámetros, fruto de la ejecución de la función.

def mi_funcion():
    print("Entra en mi_funcion")
    return
    print("No llega")
print (mi_funcion()) # Entra en mi_funcion

def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")
saludar("Ivan", "Buenos días")


