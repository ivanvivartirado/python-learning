# For se utiliza para iterar sobre una secuencia (Numeros, Cadenas de texto, Listas, etc)

# Bucle que recorre del 1 al 10
for i in range (1, 11):
    print(i)

# While se utiliza para ejecutar un bloque de codigo siempre y cuando la condicion sea verdadera

while True:
    opcion = input("Pulsa 1 para salir o 2 para entrar: ")
    if opcion == '1':
        print("Saliendo...")
        break  # Rompe el bucle infinito
    if opcion == '2':
        print("Bienvenido!")
        break #Rompe el bucle 