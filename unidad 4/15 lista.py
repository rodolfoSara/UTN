'''
Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.
'''

lista=[]
suma=0
while True:
    num= input('Ingrese un numero  ')
    num= int(num)
    lista.append(num)

    seguir = input('Quiere seguir agregando  ')
    if seguir == 'no':
        break

for i in range(1, len(lista), 2 ):
    suma+= lista[i]


print(suma)