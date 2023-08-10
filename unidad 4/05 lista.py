'''
Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.
'''

i=0
listaCiudad=[]
while i < 5:
    ciudad = input('Ingrese una ciudad ')
    listaCiudad.append(ciudad)
    i+=1

print(ciudad[-1])