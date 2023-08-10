'''

Dada una lista de números,
 imprimir todos los números que son mayores que el promedio de la lista.

'''

lista =[10,25,12,18,45,80]
i=0
j=0
suma=0
promedio=0
mayor=[]

while i < len(lista):
    suma= suma + lista[i]
    i+=1
print(suma)
print(i)
promedio = suma / i
print(f'promedio: {promedio}')

while j < len(lista):
    if lista[j] > promedio:
        print(j)
        mayor.append(lista[j])
    j+=1

print(f'Los numeros mayores al promedio son {mayor}')
