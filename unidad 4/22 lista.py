'''
Crear un programa que solicite al usuario ingresar:
nombre del producto, cantidad y precio unitario.
Guardar los datos en 3 listas distintas.
Solicitar productos hasta que el nombre del producto sea ‘xxx’.
Luego imprimir la lista de artículos con el siguiente formato:

'''
nombre_articulo=[]
cantidad=[]
precio_unitario=[]

while True:
    nombre= input('Ingrese nombre ')
    if nombre == 'xxx':
        break
    nombre_articulo.append(nombre)

    cant= input('Ingrese Cantidad ')
    cant= int(cant)
    cantidad.append(cant)

    precio = input('Ingrese el precio ')
    precio= int(precio)
    precio_unitario.append(precio)

print(f'nombre_articulo[i] cantidad precio_unitario Total ' )
for i in range(len(nombre_articulo)):
    print(f'{nombre_articulo[i]} {cantidad[i]} {precio_unitario[i]} {cantidad[i] * precio_unitario[i] }  \n' )