'''
Crea un diccionario que contenga el nombre como clave y el puntaje como valor de varios jugadores en un juego.
Luego, pedirle al usuario el nombre del jugador y nuevo puntaje y actualizar el valor correspondiente en el diccionario.
'''

jugador = {'Olaf': 10, 'mefisto': 9, 'gigalmesh':8, 'thot':6 }

for key, value in jugador.items():
    print(key, value)

nombre = input('Nombre del jugador ')
nuevoPuntaje = input('Escriba nuevo puntaje')

for key, value in jugador.items():
    if nombre == key:
        jugador[key] = nuevoPuntaje

for key, value in jugador.items():
    print(key, value)