# Building abstractions with Functions

def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'


def run():
    print(nombre_completo('Grecia', 'Corona'))
    print(nombre_completo('Grecia', 'Corona', inverso=True))
    print(nombre_completo(apellido='Corona', nombre='Grecia'))


if __name__ == "__main__":
    run()