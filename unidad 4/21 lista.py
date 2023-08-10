'''
Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos.
Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.
'''

listaPrecio=[]
listaCant=[]
for i in range(5):
    precio = input('Ingrese precio ')
    listaPrecio.append(precio)
    cant = input('Ingrese cantidad ')
    listaCant.append(cant)

for i in range(len(listaCant)):
    print(f' la cantidad es {listaCant[i]} - precio: {listaPrecio[i]}')