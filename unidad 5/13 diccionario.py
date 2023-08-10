'''
Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa.
Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres
'''

juegos ={'Royal': 5, 'Mario Bros': 4, 'GT': 7, 'Mortal Kombat': 5, 'Need for speed': 4}
dificultad = input('Dificultad: ')
dificultad = int(dificultad)
igualdad=[]

for x, j in juegos.items():
    if j == dificultad:
        igualdad.append(x)

print(igualdad)

