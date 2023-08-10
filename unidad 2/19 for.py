'''
Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.
'''

palabras=['kjñsadf', 'Hola', 'aPendice', 'fffff', 'kjhadsf', 'guarIda']
letraMayus=[]
for palabra in palabras:
    for letra in palabra:
        if letra.isupper():
            letraMayus.append(palabra)
            break

print(f'Palabras con letra mayuscula {letraMayus}')
