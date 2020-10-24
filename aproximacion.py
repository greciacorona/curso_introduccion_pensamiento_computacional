# Check if a number is a perfect square with approximation algorithm

objetivo = int(input('Escoge un número: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    r = respuesta**2 - objetivo
    print(f'No se encontró la raíz cuadrada del {objetivo}')
else:
    r = respuesta**2 - objetivo
    print(f'La raíz cuadrada del {objetivo} es {respuesta}')
