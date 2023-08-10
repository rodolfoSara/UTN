'''
Dada una lista de números, imprimir la cantidad de números pares en la lista
'''

lista =[1,2,3,4,5]
contador=0

for i in lista:
    if i % 2 ==0:
        contador+=1

print(f'la cantidad de numero pares es {contador}')