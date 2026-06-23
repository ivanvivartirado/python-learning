import itertools

palos = ['Picas', 'Corazones', 'Treboles', 'Diamantes']
numeros = ['A'] + list(range(2,11)) + ['J', 'Q', 'K']

baraja = list(itertools.product(numeros, palos))

for carta in baraja :
    print (f"{carta[0]} de {carta[1]}")
