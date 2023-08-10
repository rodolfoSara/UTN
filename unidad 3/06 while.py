'''
Dado un número entero n,
imprimir la suma de todos los números pares menores o iguales a n.
'''

num = input('Escriba un numero ')
num = int(num)

i=0
suma=0
while i <= num:
    if i % 2 == 0:
        suma += i
    i+= 1

print(f'La suma de los numero pares es {suma}')