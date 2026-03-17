"""Corto circuito"""

GAS = False
ENCENDIDO = True
EDAD = 18

if not GAS and (ENCENDIDO and EDAD > 17):
    print('Puedes avanzar')
else:
    print('No puedes avanzar')
