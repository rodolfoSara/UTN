'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo,
o "El número no es primo" si el número no es primo.
'''

numero = input('Ingrese un numero ')
numero = int(numero)
contador = 0

for i in range(2, numero):
    if numero % i == 0:
        contador += 1
        break

if contador != 0:
    print('El numero no es primo')
else:
    print('El numero es primo')
