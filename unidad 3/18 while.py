'''
Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.
'''

num = input('Escriba un num ')
num = int(num)

i=0
suma=0
while i <= num:
    if i % 5 == 0:
        suma+= i
    i+=1

print(f'La suma de los numeros multiplo de 5 es {suma}')