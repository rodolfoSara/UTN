'''
Escribir un programa que le pida al usuario que ingrese un número entero,
y luego imprima "El número es divisible por 3 y por 5" si el número es divisible
por 3 y por 5, o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.
'''

numero = input('Ingrese un numero')
numero = int(numero)

if numero % 3 == 0 and numero % 5 == 0:
    print('El numero es divisible por 3 y por 5')
else:
    print('El numero NO es divisible por 3 y 5')