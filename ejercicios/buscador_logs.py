with open("ejercicios/logs.txt", "r") as f:
    lineas = f.readlines()

contador = 0
errores_encontrados = []

for linea in lineas:
    if "ERROR" in linea:
        errores_encontrados.append(linea.strip())
        contador += 1

with open("ejercicios/errores_encontrados.txt", "w") as f:
    for error in errores_encontrados:
        f.write(error + "\n")

print("Total errores:", contador)
print("Errores guardados en errores_encontrados.txt")
