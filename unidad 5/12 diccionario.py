'''
Crea un diccionario que represente una lista de las compras.
Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad.
Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

'''

compras={'Leche': 4, 'Pan': 1, 'Carne': 2, 'Arroz': 4, 'Fideo':5}

producto= input('Ingrese el producto ')

print(compras[producto])