'''
Dado un número entero n,
imprimir la suma de los números pares menores o iguales a n.

'''

numero = input('Ingrese un numero ')
numero = int(numero)
suma = 0
for i in range(numero+1):
    if i % 2 == 0:
        suma += i

print(f'La suma es {suma}')
