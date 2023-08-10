'''
Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.
'''

lista=[]

for i in range(3):
    num=input('Ingrese un numero ')
    num = int(num)
    lista.append(num)
print(lista)
num=input('Ingrese un numero ')
lista.append(num)
print(lista)
