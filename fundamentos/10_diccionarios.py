d1 = {
    "Nombre:": "Ivan",
    "Apellido:": "Vivar",
    "Edad:": 19,
    "Email:": "ivaanv23@gmail.com"    
}
# Imprimir el diccionario entero
print(d1)
# Imprimir el valor especifico de una key
print(d1["Nombre:"])

# Iterar en un diccionario
for x in d1:
    print (d1[x])

# Si queremos imprimir claves y valores 

for x, y in d1.items():
    print (x, y)