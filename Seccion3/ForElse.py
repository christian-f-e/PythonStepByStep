"""For Else"""

buscar = 13

for item in range(5):
    print(item)
    if item == buscar:
        print('encontrado: ', buscar)
        break
    else:
        print('no encontre el numero buscado')
