'''
Dada una lista de números, imprimir el número más pequeño de la lista.

'''

listaNumeros = [80,28,3,8,15,25,4]
flag= True

for i in listaNumeros:
    if flag == True:
        numeroPeque= i
        flag = False
    elif numeroPeque > i:
        numeroPeque = i

print(f'El numero mas pequeño es {numeroPeque}')
