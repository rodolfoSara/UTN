'''

Dada una lista de números, imprimir todos los números que son múltiplos de 3.

'''

listaNum=[15,18,11,17,21, 5 ,4, 9]
listaMultiploTres=[]
i=0

while i < len(listaNum):
    if listaNum[i] % 3 ==0:
        listaMultiploTres.append(listaNum[i])
    i+=1

print(f'Los numeros multiplos de 3 son {listaMultiploTres}')
