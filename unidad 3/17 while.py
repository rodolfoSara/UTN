'''
Dada una cadena de texto, imprimir la cadena al revés.
'''

cadena = 'Dada una cadena de texto, imprimir la cadena al revés.'
reves=[]
i=len(cadena) - 1
print(i)


while i > -1:
    reves.append(cadena[i])
    i-=1

print(reves)