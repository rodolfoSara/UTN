'''
Escribir un programa que le pida al usuario 
que ingrese un número entero, y luego imprima
 "El número ingresado es par" 
 si el número es divisible por 2,
   o "El número ingresado es impar" 
   si el número no es divisible por 2.
'''
numero = input('Ingrese un nujmero')
numero = int(numero)
while True:
    if numero < 0:
        numero = input('Ingrese un numero positivo')
    else:
        break

if numero % 2 == 0:
    print('el número es par')
else:
    print('El número es impar')