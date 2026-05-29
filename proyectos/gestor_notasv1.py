# Version procedural simple, gestion de notas
print ("-----------------------------")
print ("Que quieres hacer?")
print ("1. Ver notas")
print ("2. Agregar nota")
print ("3. Salir")
print ("-----------------------------")
opcion = input ("Elige una opcion:")

if opcion == "1":
    with open ("proyectos/agenda.txt", "r") as f:
        print (f.read())
elif opcion == "2":
    with open ("proyectos/agenda.txt", "a") as f:
        nota = input ("Escribe tu nota: ")
        f.write(nota + "\n")
    print ("Nota guardada.")
elif opcion == "3":
    print("Hasta luego.")