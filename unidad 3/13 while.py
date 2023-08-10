'''
Dada una lista de números, imprimir la cantidad de números negativos en la lista.
'''

listaNum=[-1, 5, -8, 9, -19]

i=0
cantidad=0
while i < len(listaNum):
    if listaNum[i] < 0:
       cantidad+=1
    i+=1
print(f'La cantidad de numeros negativos son {cantidad}')