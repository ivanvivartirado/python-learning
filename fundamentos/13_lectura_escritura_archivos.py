# Escribir en un archivo
with open ("notas.txt", "w") as f:
    f.write("Hola mundo aqui desde alemania")

# Leer un archivo
with open ("notas.txt", "r") as f:
    contenido = f.read()
    print(contenido)