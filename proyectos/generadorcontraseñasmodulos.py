import random
import string
import os
from datetime import datetime

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

longitud = int(input("Longitud de la contraseña: "))
contraseña = generar_contraseña(longitud)
print("Contraseña:", contraseña)

# Guardar en archivo con fecha
os.makedirs("proyectos", exist_ok=True)
with open("proyectos/contraseñas.txt", "a") as f:
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    f.write(f"{fecha} — {contraseña}\n")

print("Guardada en proyectos/contraseñas.txt")
