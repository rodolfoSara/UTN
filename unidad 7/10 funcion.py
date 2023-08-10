'''Crea una función que reciba como parámetros una lista de palabras y
devuelva la palabra más larga.
'''

def palabra_mas_larga(lista):
    '''
    :param lista:
    :return: palabra mas larga de la lista
    '''
    indiceMasLargo = 0

    for i in range(len(lista)):
        if len(lista[i]) > len(lista[indiceMasLargo]):
            indiceMasLargo = i
    return lista[indiceMasLargo]

lista =['a', 'bbbbbbbbbb', 'c', 'd', 'rrrrrrrrrrrrrrrrrrrrrrrrr']
palabraLarga = palabra_mas_larga(lista)

print(f'La palabra mas larga es {palabraLarga}')
