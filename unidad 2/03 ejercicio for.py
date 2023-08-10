'''
Dado un número entero n,
imprimir la secuencia de números pares menores o iguales a n.

'''
numero = input('Ingrese un numero ')
numero = int(numero)

for i in range (numero + 1):
    if i % 2 == 0:
        print(i)