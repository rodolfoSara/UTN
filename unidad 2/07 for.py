'''
Dado un número entero n, imprimir la secuencia
de números impares menores o iguales a n.

'''

numero = input('Ingrese un numero ')
numero = int(numero)

for i in range(numero):
    if i % 2 == 1:
        print(i)