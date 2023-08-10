'''
Solicitar al usuario números enteros hasta que ingrese el 0.
Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())
'''

lista=[]
mayor=0
while True:
    num= input('Ingrese un numero ')
    num = int(num)
    if num == 0:
        break
    lista.append(num)

for i in range(len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]

print(f'El numeto mayr es {mayor}')