"""X args"""


def Suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


Suma(2, 5, 7)
Suma(1,2,3,4,5)
