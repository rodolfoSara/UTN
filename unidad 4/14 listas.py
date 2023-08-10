'''
Crea dos listas de 10 números enteros cada una
y realiza una multiplicación de los elementos con el mismo índice en ambas listas.
'''

lista1=[]
lista2=[]
resultadoLista=[]
for i in range(10):
    num = input('Ingrese un numero ')
    num= int(num)
    lista1.append(num)

for i in range(10):
    num = input('Ingrese un numero ')
    num = int(num)
    lista2.append(num)


for i in range(4):
    resultado = lista1[i] * lista2[i]
    resultadoLista.append(resultado)

print(resultadoLista)