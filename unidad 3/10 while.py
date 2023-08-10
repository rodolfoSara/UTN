'''
Dada una lista de números, imprimir la cantidad de números pares en la lista.
'''

num = input('Escriba un numero ')
num = int(num)

i = 1
numPar=[]
while i <= num:
    if i % 2 == 0:
        numPar.append(i)
    i+=1

print(f'Los numero pares son {numPar}')
