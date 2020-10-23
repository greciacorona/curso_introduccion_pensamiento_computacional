# Check if a number is a perfect square with exhaustive enumeration

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'El objetivo no tiene una raíz cuadrada exacta')
