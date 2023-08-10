'''
Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres un niño" si la edad es menor a 12,
"Eres un adolescente" si la edad está entre 12 y 17 inclusive,
"Eres un adulto" si la edad está entre 18 y 64

'''

edad = input('Ingrese una edad ')
edad = int(edad)

if edad < 12:
    print('Eres un niño')
elif edad > 12 and edad < 18:
    print('Eres un adolescente')
else:
    print('Eres una adulto')