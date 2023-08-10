'''
Dada una lista de palabras, imprimir las palabras que tienen una letra específica.
'''


listaPalabras=['Hola', 'wie', 'sss', 'dddd', 's', 'obtuso', 'danke']
letra = input('Letra que quiere buscar ')
palabrasConLetra =[]


for i in listaPalabras:
    if letra in i:
        palabrasConLetra.append(i)

print(f'Las palabras impar son {palabrasConLetra} ')