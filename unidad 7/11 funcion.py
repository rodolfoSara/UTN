'''
Crea una función que reciba como parámetro una cadena de texto y devuelva
la cantidad de vocales que tiene.
'''


def cantidad_vocales(cadenaTexto):
    '''
    :param cadenaTexto:
    :return: cantidad de volcaes que tiene la cadena
    '''

    cadenaTexto= cadenaTexto.lower()
    vocales=['a', 'e', 'i', 'o', 'u']
    cantidad=0
    for i in cadenaTexto:
        if i in vocales:
            cantidad += 1
    return cantidad

cadenaTexto ='Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.'

cantidadVocales = cantidad_vocales(cadenaTexto)

print(f'La cantidad de vocales en la cadena son {cantidadVocales}')