# En proceso de crear una calculadora con distintas funciones 
# Preguntamos por la operacion que quiere realizar el usuario dejando claro las opciones
funcion = input ("Introduce la operacion que quieres realizar(Suma, Resta, Multiplicacion, Division):")

num1 = int(input ("Introduce el primer numero:"))
num2 = int(input ("Introduce el segundo numero:"))

# Por si el usuario introduce una opreacion no valida
if funcion not in ("Suma", "Resta", "Multiplicacion", "Division"):
    print("Error la opcion no es valida, por favor introduzca: Suma, Resta, Multiplicacion, Division")

if funcion == "Suma":
    resultado = num1 + num2
    print("El resultado de la suma es: ",resultado)

if funcion == "Resta":
    resultado = num1 - num2
    print("El resultado de la resta es:" ,resultado)

if funcion == "Multiplicacion":
    resultado = num1 * num2
    print("El resultado de la multiplicacion es:" ,resultado)

if funcion == "Division":
    resultado = num1/num2
    print("El resultado de la division es:" ,resultado)

