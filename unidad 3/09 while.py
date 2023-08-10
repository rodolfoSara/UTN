'''
Dado un número entero n, imprimir todos los números impares menores o iguales a n.
'''

num = input('Escriba un numero ')
num = int(num)

i=0
numImpar=[]

while i <= num:
    if i % 2 == 1:
        numImpar.append(i)
    i+=1

print(f'los numero impar son {numImpar}')