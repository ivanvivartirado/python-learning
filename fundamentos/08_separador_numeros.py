#FUNDAMENTO: SEPARADORES DE NÚMEROS EN PYTHON (Underscores en literales)

#En Python, puedes usar el guion bajo (_) como separador visual en 
#números grandes para que sean mucho más fáciles de leer.
#Python ignora completamente estos guiones bajos al ejecutar el código.

# 1. Números enteros grandes (equivale a usar puntos o comas en contabilidad)
un_millon = 1_000_000
diez_mil_millones = 10_000_000_000

print("--- 1. Enteros Grandes ---")
print(f"Un millón escrito como 1_000_000: {un_millon}")
print(f"Diez mil millones escrito como 10_000_000_000: {diez_mil_millones}")
print()

# 2. Números decimales (float)
precio = 15_450.75
pi_largo = 3.14159_26535_89793

print("--- 2. Decimales ---")
print(f"Precio (15_450.75): {precio}")
print(f"Pi con separadores: {pi_largo}")
print()

# 3. Otros sistemas numéricos (Binario, Hexadecimal)
# Es súper útil para agrupar bytes u octetos.
binario = 0b1100_1010_1111_0000
hexadecimal = 0xFF_AA_BB_00

print("--- 3. Otros Sistemas ---")
print(f"Binario (0b1100_1010_1111_0000): {binario}")
print(f"Hexadecimal (0xFF_AA_BB_00): {hexadecimal}")
print()


#Reglas importantes:
# - No puedes poner dos guiones bajos seguidos (ej. 1__000 da SyntaxError).
# - No puedes empezar ni terminar un número con guion bajo (ej. _100 o 100_).
# - No puedes ponerlo justo al lado del punto decimal (ej. 3._14).
