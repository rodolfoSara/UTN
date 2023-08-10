'''
Crea una lista de números y encuentra el promedio de todos los números en la lista.
'''

lista=[]
suma=0
contador=0
while True:
    num= input('Ingrese un numero  ')
    num= int(num)
    lista.append(num)
    suma+= num
    contador+=1
    seguir = input('Quiere seguir agregando  ')
    if seguir == 'no':
        break

promedio = suma / contador

print(f'El promedio es {promedio}')