'''
14. Crear una función que recibe una lista de números y devuelve un diccionario
con el valor mínimo, el valor máximo y el promedio de los números en la lista.
'''


def promedio_maximo_minimo(lista:list):
    '''
    :param lista:
    :return: diccionario con promedio, maxio y minimo de la lita de numeros
    '''
    maximo = 0
    minimo =0
    suma = 0

    diccionario = {}
    for i in range(len(lista)):
        if lista[i] > lista[maximo]:
            maximo = i
        elif lista[i] < lista[minimo]:
            minimo = i

        suma += lista[i]
        print(suma)

    promedio = float(suma / len(lista))

    diccionario = {'Promedio': promedio, 'Maximo':lista[maximo], 'Minimo': lista[minimo] }
    return diccionario


lista =[10, 20, 30, 98, 74, 65]
print(promedio_maximo_minimo(lista))