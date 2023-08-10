'''
Dada una lista de números, imprimir el número más grande de la lista.

'''
lista = [55,2,40,4,5,6]


num = lista[0]
for i in range(len(lista)):
    if lista[i] > num:
        num = lista[i]

print(f'El numero mas grande es {num}')