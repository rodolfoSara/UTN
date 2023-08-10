'''
Dada una lista de números, imprimir la suma de todos los elementos de la lista.
'''

lista =[1,2,3,4,5]

i=0
suma=0
while i <= len(lista):
    suma+= i
    i+=1
print(f'La suma de todos los numeros es {suma}')