'''
Crea una lista con los nombres de tus 3 películas favoritas
y luego imprime los elementos en orden inverso (sin utilizar el método reverse())
'''

listaPelis=[]

for i in range(3):
    pelis=input('Ingrese una peli ')
    listaPelis.append(pelis)

print(listaPelis)

for i in listaPelis[:: -1]:
    print(i)