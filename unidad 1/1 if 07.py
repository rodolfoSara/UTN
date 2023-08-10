'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo,
 o "El número no es primo" si el número no es primo.

'''

numero = input('Escriba un numero ')
numero = int(numero)

while True:
    if numero < 1:
        input('Escriba de nuevo')
    else:
        break

contador = 0
for n in range(2, numero):
    if numero % n == 0:
        contador+= 1
        if contador > 0:
            break

if contador == 0:
    print('Numero primo')
else:
    print('Numero no primo')




