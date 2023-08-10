'''
Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo.
Luego, muestra la suma de todos los números ingresados.
'''
lista=[]
suma=0
while True:
    num = input('Ingrese un numero ')
    num= int(num)
    if num < 0:
        break
    lista.append(num)


for i in lista:
    suma+= i
print(lista)
print(f'La suma de los numero {suma}')

