'''
Crear una función que calcule el promedio de edad de un grupo de personas.
Recibe una lista de edades y devuelve el promedio.
'''

def promedio_edad(lista):
    '''

    :param lista:
    :return: promedio de edad
    '''
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    return promedio

lista = [10,20,30,40,45]

promedioEdad = promedio_edad(lista)

print(f' El promedio de edad {promedioEdad}')


