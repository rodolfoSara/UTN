'''
Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.
'''

letra = input('Ingrese un letra ')

cadena = 'Si, pero quién nos curarà del fuego sordo, del fuego sin color que corre al anochecer por la rue de la Huchette, saliendo de los portales carcomidos, de los parvos zaguanes, del fuego sin imagen que lame las piedras y acecha en los vanos de las puertas'
cadena= cadena.lower()
i=0
cantidad=0
while i < len(cadena):
    if cadena[i] == letra:
        cantidad+=1
    i+=1
print(f'La cantidad de letras {letra} en la oracion es de {cantidad}')