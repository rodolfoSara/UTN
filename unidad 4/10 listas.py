'''
Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.
'''

lista=[]
lista5Palabras=[]

while True:
    palabra= input('Ingrese un palabra  ')
    lista.append(palabra)

    seguir = input('Quiere segui agregando  ')
    if seguir == 'no':
        break

for i in range(len(lista)):
    if len(lista[i]) > 5:
        lista5Palabras.append(lista[i])
print(lista)
print(lista5Palabras)
