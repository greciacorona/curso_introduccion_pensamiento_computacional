def factorial(n):
    """
    Calcula el factorial de n.

    Args:
        n (int) > 0
    Return:
        !n
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1) 


def run():
    n = int(input('Escribe un entero: '))
    print(factorial(n))
    

if __name__ == "__main__":
    run()