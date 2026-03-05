"""Argumentos Nombrados"""

nombre = 'Christian'
apellido = 'Fernandez'


def Hola(nombre, apellido="Feliz"):
    print('Hola Mundo')
    print(f'Bienvenido {nombre} {apellido}')


Hola(nombre, apellido)
Hola('Chachito')

Hola(apellido='Fernandez',nombre='Christian')