contraseña = input ("Introduce tu contraseña:")

tiene_numero = False
tiene_mayuscula = False
tiene_minuscula = False
tiene_especial = False
tiene_longitud = len(contraseña) > 8

for caracter in contraseña:
    if caracter .isdigit():
        tiene_numero = True
    if caracter .isupper():
        tiene_mayuscula = True
    if caracter .islower():
        tiene_minuscula = True
    if not (caracter .isalnum()):
        tiene_especial = True

reglas = tiene_longitud + tiene_numero + tiene_mayuscula + tiene_minuscula + tiene_especial

if reglas == 5:
    print ("Tu contraseña es fuerte")
elif reglas >= 3:
    print ("Tu contraseña es media")
else:
    print ("Tu contraseña es debil")
