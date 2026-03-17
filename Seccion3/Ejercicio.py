"""Ejercicio"""
# numero = 0
# opcion = ""
# siguiente = 'Porfavor ingresa el siguiente numero'

RESULTADO = ""

print('Bienvenidos a la calculadora')
print('Para salir escribe salir')
print('Las operaciones son suma, multi, div y resta')


while True:
    if not RESULTADO:
        RESULTADO = input('Ingrese un numero: ')
        if RESULTADO.lower() == 'salir':
            break
        RESULTADO = int(RESULTADO)
    op = input('Ingresa operacion: ')
    if op.lower() == 'salir':
        break
    n2 = input('Ingresa el siguiente núemro: ')
    if n2.lower() == 'salir':
        break
    n2 = int(n2)

    if op.lower() == 'suma':
        RESULTADO += n2
    elif op.lower() == 'resta':
        RESULTADO -= n2
    elif op.lower() == 'multi':
        RESULTADO *= n2
    elif op.lower() == 'div':
        RESULTADO /= n2
    else:
        print('Operacion no valida')
        break

    print(f"El resultado es: {RESULTADO}")

# while opcion.lower() != 'salir':
#     if numero == 0:
#         numero = int(input("por favor proporciona un numero: "))
#         if numero >= 0:
#             opcion = input("Profavor ingrese una operacion: ")
#             if opcion.lower() == 'suma':
#                 numero += int(input(f"{siguiente}: "))
#             elif opcion.lower() == 'resta':
#                 numero -= int(input(f"{siguiente}: "))
#             elif opcion.lower() == 'multi':
#                 numero *= int(input(f"{siguiente}: "))
#             elif opcion.lower() == 'div':
#                 numero /= int(input(f"{siguiente}: "))
#     print(f'El resultado es {numero}')
#     numero = 0
