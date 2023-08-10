'''
Crea un diccionario que represente las notas de un examen de varios estudiantes,
donde las claves son los nombres de los estudiantes y los valores son sus notas.
Imprime el promedio de las notas.
'''

estudiantes = {'Rod': 8, 'Pepo': 9, 'Ruth': 9, 'Carmen': 7, 'Pulgas':2}
suma=0
cant=0

for i in estudiantes:
    suma+= estudiantes[i]
    cant+=1


promedio = suma / cant
print(promedio)