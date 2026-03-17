"""Argumentos Nombrados"""

NOMBRE = 'Christian'
APELLIDO = 'Fernandez'


def hola(nombre, apellido="Feliz"):
    """concatena nombre y apellido"""
    print('Hola Mundo')
    print(f'Bienvenido {nombre} {apellido}')


hola(NOMBRE, APELLIDO)
hola('Chachito')

hola(apellido='Fernandez', nombre='Christian')
