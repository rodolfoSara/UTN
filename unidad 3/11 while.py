'''
Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.
'''

oracion = ['pppppprrrr','Dada', 'una', 'lista', 'palabras', 'hhhhhhuu']

i=0
palabrasMas5carac=[]

while i < len(oracion):
    if len(oracion[i]) > 5:
        palabrasMas5carac.append(oracion[i])
    i+=1

print(f'Las plabras con mas de 5 caracteres son {palabrasMas5carac}')