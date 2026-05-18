with open("ejercicios/ip.txt", "r") as f:
    lineas = f.readlines()

contador = 0

for linea in lineas:
    if "192.168" in linea:
        print("Ip encontrada:", linea.strip())
        contador += 1

print ("Total de ips 192.168 encontradas: ", contador)