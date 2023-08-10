'''
Crear una función que cuente la cantidad de veces que aparece un elemento
en una lista. Recibe una lista y un elemento como parámetros y devuelve la
cantidad de veces que aparece en la lista.
'''

def cantidad_elementos_lista(lista):
    '''

    :param lista:
    :return: un diccionario con el elemento (key) y la cantidad (value) de veces q aparece
    '''
    elementos_y_cantidad = {}
    for i in lista:
        if i in elementos_y_cantidad:
            elementos_y_cantidad[i] += 1
        else:
            elementos_y_cantidad[i] = 1

    return elementos_y_cantidad


lista = ['hola', 'hola', 'q', 'a', 'a', 'b', 'a']


cantidad = cantidad_elementos_lista(lista)
print(cantidad)

