'''
Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.
'''
lista1=[1,6,7,3,4]
lista2=[2,8,1,7,4]
listaComunes=[]

for i in range(len(lista1)):
    for j in range(len(lista2)):
        if lista1[i] == lista2[j]:
            listaComunes.append(lista2[j])

print(listaComunes)