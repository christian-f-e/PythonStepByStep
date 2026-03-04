"""Iterables"""

buscar = 13

for item in range(5):  # iterable
    print(item)
    if item == buscar:
        print('encontrado: ', buscar)
        break
    else:
        print('no encontre el numero buscado')

for char in "Ultimate Python":  # iterable
    print(char)
