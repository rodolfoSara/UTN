'''
Crear una función que recibe una lista de palabras y devuelve un diccionario
con las palabras como llaves y su longitud como valores.
'''

def lista_to_dictionary(lista):
    '''
    :param lista:
    :return: diccionariop con la palabra y un largo
    '''
    diccionario = {}
    for i in lista:
        longitud = len(i)
        diccionario[i] = longitud
    return diccionario

lista = ['maca', 'pimby', 'pulgas', 'ruth', 'Herta']

diccionario = lista_to_dictionary(lista)

print(diccionario)