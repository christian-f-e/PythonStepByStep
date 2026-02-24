"""CalculadoraBasica.py"""
n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa secundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
rest = n1 - n2
mult = n1 * n2
divi = n1 / n2

output = f"""
Para los números {n1} y {n2}
el resultado de la suma es {suma}.
el resultado de la resta es {rest}.
el resultado de la multiplicacion es {mult}.
el resultado de la divicion es {divi}.
"""

print(output)
