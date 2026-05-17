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
resta(5, 3)
print(resta(5, 3))

# Argumentos por defecto

def suma (a, b, c=20):
    return a+b+c
suma (5,5) # Dado que el parámetro c tiene un valor por defecto, la función puede ser llamada sin ese valor.

print (suma (5, 5))

# Asignar valor por defecto a todos los parametros

def sumapred(a=3, b=5, c=0):
    return a+b+c
sumapred() 
print (sumapred())

