'''
Dado un número entero n,
 imprimir la secuencia de números primos menores o iguales a n.

'''

numero = input('Ingrese un numero ')
numero = int(numero)

contador=0
primos=[]

for i in range(1,numero):
    if i % 2 == 1:
        primos.append(i)

print(primos)