def primera_letra(lista_de_palabras):
    """Ejemplo de Afirmaciones en Python.

    Args:
        lista_de_palabras ([str]): [lista de palabras]
        assert <expresion booleana>, <mensaje de error>

    Returns:
        [str]: [devuelve la primera letra de la lista]
    """    
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, 'No se permiten strings vacíos'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)
        
    return primeras_letras

# print(primera_letra.__doc__)


def run():
    lista = ['pan', 5.7, 'mantequilla', '', 'azúcar', True, 'cafe']
    print(primera_letra(lista))


if __name__ == "__main__":
    run()