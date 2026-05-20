import os

print(os.getcwd())          # carpeta actual
print(os.listdir("."))      # archivos de la carpeta actual
print(os.name)              # 'nt' = Windows, 'posix' = Linux/Mac
print(os.path.exists("proyectos/agenda.txt"))  # True o False
# Crear una carpeta
os.makedirs("proyectos/backups", exist_ok=True)
print("Carpeta creada")

# Renombrar un archivo
# os.rename("viejo.txt", "nuevo.txt")

# Borrar un archivo
# os.remove("archivo.txt")

# Tamaño de un archivo en bytes
tamaño = os.path.getsize("notas.txt")
print("Tamaño:", tamaño, "bytes")

# Saber si algo es archivo o carpeta
print(os.path.isfile("notas.txt"))     # True = es archivo
print(os.path.isdir("proyectos"))      # True = es carpeta

# Unir rutas de forma segura (mejor que concatenar strings)
ruta = os.path.join("proyectos", "agenda.txt")
print("Ruta:", ruta)

from datetime import datetime

# Fecha y hora actual
ahora = datetime.now()
print(ahora)

# Formatear la fecha como quieras
print(ahora.strftime("%d/%m/%Y"))           # 20/05/2026
print(ahora.strftime("%H:%M:%S"))           # 14:32:10
print(ahora.strftime("%d/%m/%Y %H:%M"))     # 20/05/2026 14:32

# Extraer partes por separado
print("Día:", ahora.day)
print("Mes:", ahora.month)
print("Año:", ahora.year)
print("Hora:", ahora.hour)
print("Minuto:", ahora.minute)

import random

# Número aleatorio entre dos valores
print(random.randint(1, 100))

# Elemento aleatorio de una lista
colores = ["rojo", "azul", "verde", "amarillo"]
print(random.choice(colores))

# Mezclar una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numeros)
print(numeros)

# Muestra aleatoria de N elementos
print(random.sample(colores, 2))

# Decimal aleatorio entre 0 y 1
print(random.random())