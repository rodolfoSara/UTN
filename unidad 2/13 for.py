'''
Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.
'''

listaPalabras=['Hola', 'wie', 'sss', 'dddd', 's']
palabrasImpar=[]

for i in listaPalabras:
    if len(i) % 2== 1:
        palabrasImpar.append(i)

print(f'Las palabras impar son {palabrasImpar} ')
