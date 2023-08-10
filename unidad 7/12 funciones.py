'''
Crea una función que reciba dos listas de nombres, y devuelva una lista con
los nombres que aparecen en ambas listas
'''

def nombre_repetidos(listaNombre1, listaNombre2):
    '''

    :param listaNombre1:
    :param listaNombre2:
    :return: un lista nueva con nombre q se repiten
    '''
    listaRepetidos=[]
    for i in listaNombre1:
        if i in listaNombre2:
            listaRepetidos.append(i)
    return listaRepetidos


listaNombre1 = ['maca', 'pimby', 'pulgas', 'ruth', 'Herta']

listaNombre2 = ['maca', 'pimby', 'Rin', 'Carmen', 'Herta']

repetidos = nombre_repetidos(listaNombre1, listaNombre2)

print(f'Los nombres repetidos son {repetidos}')