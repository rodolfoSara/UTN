'''
Crear una función que convierta grados Celsius a grados Fahrenheit.
 Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

'''
def celsius_a_fahrenheit(grados):
    '''
    recibe celsius
    :param grados: celsius
    :return: celsius to farenheit
    '''
    convertir = grados * 1.8 + 32
    return convertir

grados = int(input('escriba los grados '))

grados_fahreinheit = celsius_a_fahrenheit(grados)

print(f'De celsius a farenheit {grados_fahreinheit}')