'''
Crea una lista de números enteros y pide al usuario que ingrese otro número entero.
Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra.
Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró
'''

listaNum=[]

while True:
    num= input('Ingrese un numero  ')
    listaNum.append(num)
    seguir = input('Quiere segui agregando numero ')
    if seguir == 'no':
        break

buscar= input('Ingrese ')
for i in range(len(listaNum)):
    if buscar == listaNum[i]:
        print(f'el numero {buscar} esta en la posicion {i}')