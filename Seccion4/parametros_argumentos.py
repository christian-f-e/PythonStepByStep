"""parametros_y_argumentos.py"""

NOMBRE = 'Christian'
APELLIDO = 'Fernandez'


def hola(nombre, apellido):
    """concatena nombre y apellido"""
    print('Hola Mundo')
    print(f'Bienvenido {nombre} {apellido}')


hola(NOMBRE, APELLIDO)
hola('Chachito', 'Feliz')
