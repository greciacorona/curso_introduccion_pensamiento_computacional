# Programa que compara las edades de 2 usuarios
# y menciona quién de los usuarios es mayor
# Pregunta nombre y edad

def calcula_edad(edad_1, edad_2, nombre_1, nombre_2):
    if edad_1 > edad_2:
        return (f'{nombre_1} es mayor que {nombre_2}')
    elif edad_1 < edad_2:
        return (f'{nombre_2} es mayor que {nombre_1}')
    else:
        return (f'Tienen la misma edad {nombre_1} y {nombre_2}')


def run():
    nombre_1 = input('Nombre de la 1ra persona: ')
    edad_1 = int(input(f'Edad de {nombre_1}: '))
    nombre_2 = input('Nombre de la 2da persona: ')
    edad_2 = int(input(f'Edad de {nombre_2}: '))

    print(calcula_edad(edad_1, edad_2, nombre_1, nombre_2))


if __name__ == "__main__":
    run()