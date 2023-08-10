'''
Crea un diccionario que represente las edades de varias personas,
donde las claves son los nombres de las personas
y los valores son sus edades. Imprime la edad de la persona más joven.
'''

personas={'Carmen': 60, 'Ruth': 50, 'Martin': 60, 'Pulgas': 7}
flag= False

for i in personas:
    if flag == False:
        flag = True
        edadJoven = personas[i]
    elif edadJoven > personas[i]:
        edadJoven = personas[i]

print(f'La edad es mas joven {edadJoven}')
