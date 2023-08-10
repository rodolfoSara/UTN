'''
Crear una función que verifique si un número es par o impar. Recibe un
número como parámetro y devuelve True si es par o False si es impar.
'''


def par_o_impar(numero):
    '''
    :param numero:
    :return: si es par o no
    '''
    if numero % 2 == 0:
        return True
    else:
        return False

numero = input('Ingrese un numero ')
numero = int(numero)

parOimpar = par_o_impar(numero)

print(f'El numero es Par: {parOimpar}')