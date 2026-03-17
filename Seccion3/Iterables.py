"""Iterables"""

BUSCAR = 13

for item in range(5):  # iterable
    print(item)
    if item == BUSCAR:
        print('encontrado: ', BUSCAR)
        break
    else:
        print('no encontre el numero buscado')

for char in "Ultimate Python":  # iterable
    print(char)
