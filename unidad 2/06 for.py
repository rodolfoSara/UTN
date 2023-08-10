'''
Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

'''

vocales= ['a', 'e', 'i', 'o', 'u']

palabrasLista = ['hola', 'wie gehts', 'oo']
contador=0
for i in palabrasLista:
    for j in i:
        if j in vocales:
            contador+=1

print(f'La cantidad de vocales es {contador}')

