'''
Crear una función que calcule el máximo común divisor de dos números.
Recibe dos parámetros (números) y devuelve el máximo común divisor.
'''

def maximo_comun_divisor(num1, num2):
    '''
    :param num1:
    :param num2:
    :return: divisor comun
    '''
    while (num2 != 0):
        temporal = num2
        num2 = num1 % num2
        num1 = temporal
    return num1

num1 = input('Ingrese numero 1 ')
num1 = int(num1)

num2 = input('Ingrese numero 2 ')
num2 = int(num2)

mcd = maximo_comun_divisor(num1, num2)

print(f'el Maximo comun divisor es {mcd}')