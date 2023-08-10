'''
Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

'''

vocales = ['a', 'e', 'i', 'o', 'u']

cadena = 'Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.'

i=0
j=0
cantidad=0


while i in range(len(cadena)):
    if cadena[i] in vocales:
        cantidad+=1
    i+=1

print(f'La cantidad de vocales son {cantidad}')