"""For Else"""

BUSCAR = 13

for item in range(5):
    print(item)
    if item == BUSCAR:
        print('encontrado: ', BUSCAR)
        break
    else:
        print('no encontre el numero buscado')
