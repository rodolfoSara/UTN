'''Dado un número entero n,
imprimir la suma de los números impares menores o iguales a n.
'''

numero = input('Ingrese un numero ')
numero = int(numero)

suma = 0;

for i in range (numero, 0 , -1):
    if i % 2 == 1:
        suma += i

print(f'La suma de los numero impares es {suma}')