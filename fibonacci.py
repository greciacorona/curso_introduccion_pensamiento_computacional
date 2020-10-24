# Fibonacci 

numeros = int(input('Dime cuantos numeros de la secuencia de Fibonacci quieres ver: '))
num1 = 0
num2 = 1

print(f'{num1}')
print(f'{num2}')
for i in range (numeros-1):
    num3 = num1 + num2
    print(f'{num3}') 
    num1 = num2
    num2 = num3


# n = int(input('Dime cuantos numeros de la secuencia de Fibonacci quieres ver: '))
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(n))