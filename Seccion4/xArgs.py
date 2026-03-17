"""xargs.py"""


def suma(*numeros):
    """Suma todos los numeros pasados como argumentos"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(1, 2, 3, 4, 5)
