'''
2. Crear una función que calcule el área de un círculo. Recibe un parámetro
(radio) y devuelve el área del círculo.

 2(pi) por radio. Área
'''

def calcular_radio(radio):
    '''
    :param radio: recibe radio
    :return: area de circulo
    '''
    area = 2 * 3.14 * radio
    return area

radio = int(input('Escriba el radio '))

resultado = calcular_radio(radio)

print(f'El area es {resultado}')