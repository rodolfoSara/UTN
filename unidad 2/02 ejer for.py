'''
Dada una lista de palabras, imprimir la palabra más larga de la lista.

'''

palabras = ['hola', 'langweilig',  'python', 'sheissen']
flaq = False

for i in palabras:
    largoPalabra = len(i)
    if flaq == False:
        masLargo = largoPalabra
        palabraLarga = i
        flaq = True
    elif largoPalabra > masLargo:
        masLargo = largoPalabra
        palabraLarga = i

print(f'La palabra mas larga es {palabraLarga} con {masLargo} caracteres')


