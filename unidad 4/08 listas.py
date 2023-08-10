'''
Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.
'''

listaLibro=[]
for i in range(5):
    libro= input('Ingrese su libros preferido ')
    listaLibro.append(libro)
for i in range(3):
    print(f'{listaLibro[i]}')