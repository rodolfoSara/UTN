'''
Crea una lista de palabras y pide al usuario que ingrese una palabra.
Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.
'''

lista=[]
listaLongitud=[]
palabrasLong=[]
'''
while True:
    palabra= input('Ingrese un palabra  ')
    lista.append(palabra)

    seguir = input('Quiere seguir agregando  ')
    if seguir == 'no':
        break
'''

#word = input('Ingrese una palabra ')

word = 'hola'
cantLetraPalabra = 0

for i in range(len(word)):
    cantLetraPalabra += i

print(cantLetraPalabra)



lista=['hola', 'querer', 'casa', 'zapato']

for palabra in lista:
    for letra in palabra:
        print(letra)

