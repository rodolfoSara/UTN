'''
Crea una lista con 5 números enteros. Luego solicita un nuevo número
y reemplaza el tercer elemento de la lista por el número ingresado.
Finalmente imprime todos los números
'''

lista=[]
for i in range(5):
    num = input('Ingrese un numero ')
    lista.append(num)
print(lista)

num = input('Ingrese un numero ')
lista[2] = num
print(lista)
