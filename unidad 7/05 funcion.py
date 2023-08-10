'''
Crear una función que determine si un número es primo o no. Recibe un
parámetro (número) y devuelve True si es primo y False si no lo es.
'''

def esPrimo(numero):
    '''
    :param numero:
    :return: si es primo o no es
    '''

    for i in range(2, numero):
        if numero % i == 0:
            primo = 'No es primo'
            break
        else:
            primo = 'Es primo'
    return primo

numero = input('Ingrese un numero ')
numero = int(numero)

primo = esPrimo(numero)

print(primo)



