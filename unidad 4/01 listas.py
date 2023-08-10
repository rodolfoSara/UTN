'''
Crea una lista con los números del 1 al 10 e imprime solo los números impares.
'''

lista=[]
listaImpar=[]

for i in range(1,11):
    lista.append(i)
    if i % 2 == 1:
        listaImpar.append(i)

print(lista)
print(f'Los pares de la lista son {listaImpar}')