'''
Crear una función que calcule el descuento aplicado a un producto. Recibe
dos parámetros (precio original y precio con descuento) y devuelve el
porcentaje de descuento aplicado.
'''

def porcetaje_descuento(precio, precioConDescuento):
    porcetajeDescuento = precioConDescuento * 100 / precio
    porcetajeDescuento = 100 - porcetajeDescuento
    return porcetajeDescuento


precio = input('Ingrese precio ')
precio = int(precio)

precioConDescuento = input('Ingrese precio con descuento')
precioConDescuento= int(precioConDescuento)

descuento = porcetaje_descuento(precio, precioConDescuento)
print(f'El descuento es de {descuento} %')