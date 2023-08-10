'''
Escribir un programa que le pida al usuario que ingrese un número entero,
y luego imprima "El número es positivo y par" si el número es positivo y divisible por 2,
o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores.

'''

numero = input('Ingrese un numero')
numero = int(numero)

if numero % 2==0  and numero > 0:
    print ('El numero es positivo y par')
elif not (numero % 2==0 and numero > 0):
    print('El numero no cumple ninguna de als dos condiciones')