# Methods of computing square roots

def exhaustive_enumeration(number):
    solution = 0

    while solution**2 < number:
        solution += 1

    if solution**2 == number:
        return f'\n The square root of {number} is {solution}'
    else:
        return f'\n The number {number} is not a perfect square number'


def approximation(number):
    epsilon = 0.01
    move = epsilon**2
    solution = 0.0

    while abs(solution**2 - number) >= epsilon and solution <= number:
        # print(abs(solution**2 - number), solution)
        solution += move

    if abs(solution**2 - number) >= epsilon:
        r = solution**2 - number
        return f'\n There is not a square root of {number}'
    else:
        r = solution**2 - number
        return f'\n The square root of {number} is {solution}'


def binary_search(number):
    epsilon = 0.01
    low = 0.0
    high = max(1.0, number)
    solution = (high + low) / 2

    while abs(solution**2 - number) >= epsilon:
        # print(f'low={low}, high={high}, solution={solution}')
        if solution**2 < number:
            low = solution
        else:
            high = solution

        solution = (high + low) / 2

    return f'\n The square root of {number} is {solution}'


def run():
    number = int(input('\n Program to get the square root of the given number. \n Enter a number: '))
    menu = """
    ✅Which method do you choose?
    1 - Exhaustive Enumeration
    2 - Approximation Algorithm
    3 - Binary Search
    """ 
    option = int(input(menu))

    if option == 1:
        print(exhaustive_enumeration(number))
    elif option == 2:
        print(approximation(number))
    elif option == 3:
        print(binary_search(number))
    else:
        print('Choose a correct option')


if __name__ == "__main__":
    run()