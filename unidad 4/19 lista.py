'''
Crea una lista vacía y pide al usuario que ingrese una palabra.
Luego, agrega la palabra a la lista si no se encuentra ya en la lista.
Repite este proceso hasta que la lista tenga al menos 5 palabras.
'''

listaPalabra=[]
contador=0

while True:
    palabra= input('Ingrese un palabra  ')
    if palabra not in listaPalabra:
        listaPalabra.append(palabra)
    contador+=1
    if contador > 4:
        seguir = input('Quiere seguir agregando  ')
        if seguir == 'no':
            break

print(listaPalabra)