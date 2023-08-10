'''
Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista
que contenga los elementos de ambas listas intercalados.
Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"],
a tercera lista debería ser [1, "a", 2, "b", 3, "c"].
'''

lista=[]
lista2=[]
lista3=[]
cant=0
cant2=0
while True:
    num= input('Ingrese un elemento  ')
    lista.append(num)

    seguir = input('Quiere seguir agregando  ')
    if seguir == 'no':
        break

print('Ingrese en otra lista')

while True:

    num= input('Ingrese un elemento  ')
    lista2.append(num)

    seguir = input('Quiere seguir agregando  ')
    if seguir == 'no':
        break

for i in range(len(lista)):
    lista3.append(lista[i])
    lista3.append(lista2[i])

print(lista3)