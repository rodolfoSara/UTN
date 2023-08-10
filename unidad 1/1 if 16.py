'''
Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
 y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive,
 "Eres adulto" si la edad está entre 18 y 64 inclusive,
 o "Eres adulto mayor" si la edad es mayor o igual a 65.

'''

edad = input('Ingrese una edad ')
edad = int(edad)

if edad < 12:
    print('Eres un niño')
elif edad > 12 and edad < 18:
    print('Eres un adolescente')
elif edad > 17 and edad < 65:
    print('Eres adulto')
else:
    print('Eres un adulto mayor')