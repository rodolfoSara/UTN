'''
Dada una lista de números,
imprimir la suma de los números en la lista que son mayores que el promedio de la lista.
'''

listaNum=[10, 15,25,58, 87]
suma=0
promedio=0
cant=0

for i in listaNum:
    suma+= i
    cant+=1

promedio = suma / cant

cant2 = 0
suma2 = 0

for num in listaNum:
    if num > promedio:
        suma2+= num
        cant2 += 1
promedio2 = suma2 / cant2

print(promedio)
print(promedio2)
