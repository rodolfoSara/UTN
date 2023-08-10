'''
Crear una función que calcule el área de un triángulo. Recibe dos parámetros
(base y altura) y devuelve el área.

b * h / 2
'''

def area_triangulo(base, altura):
    '''
    :param base
    :param altura:
    :return: area de triangulo
    '''
    area= (base * altura) / 2
    return area

base = input('Ingrese base ')
base = int(base)

altura = input('Ingrese altura ')
altura = int(altura)

areaTriangulo = area_triangulo(base, altura)

print(f'El area del triangulo es {areaTriangulo}')