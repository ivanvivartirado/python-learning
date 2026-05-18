import math # siempre arriba del todo

try: 
    numero1 = float(input("Introduce un numero para dividir:"))
    numero2 = float(input("Introduce el segundo numero:"))
    resultado = numero1 / numero2

    # Comprobamos infinito antes de dividir
    if math.isinf(numero1) or math.isinf(numero2):
        print("Error: Uno de los numeros es infinito")
        raise ValueError("No se puede dividir por infinito")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except ValueError as e:    # 'as e' captura el mensaje del error para mostrarlo
    print("Error: Introduce un numero valido", e)
else:# Solo se ejecuta si no hubo ningún error
    print ("Operacion exitosa", resultado)
finally: # Se ejecuta siempre, haya error o no
    print ("Fin del programa")


