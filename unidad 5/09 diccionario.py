'''
Crea un diccionario que contenga las capitales de los países de América del Sur.
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
'''

capitales={'Venezuela': 'Caracas', 'Colombia': 'Bogota', 'Ecuador': 'Quito', 'Peru': 'Lima', 'Chile': 'Santiago de chile', 'Argentina': 'Bs As '}

pais = input('Ingrese un pais ')

print(capitales[pais])