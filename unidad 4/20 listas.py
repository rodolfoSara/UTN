'''
A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor,
el promedio y la suma total de todos los elementos
'''
lista=[1,80,5,0,15,-5,1,79]
flag= False
suma=0

for i in range(len(lista)):
    if flag == False:
        flag = True
        mayor= lista[i]
        menor= lista[i]
    elif lista[i] > mayor:
        mayor = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
    suma+= lista[i]


promedio = suma / (i+1)

print(f'El numero mayor es {mayor}')
print(f'El numero menor es {menor}')
print(f'La suma es {suma}')
print(f'El promedio es {promedio}')
