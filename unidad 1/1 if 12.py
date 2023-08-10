'''
Escribir un programa que le pida al usuario que ingrese dos números enteros,
y luego imprima "El primer número es positivo" si el primer número es mayor que cero,
"El segundo número es positivo" si el segundo número es mayor que cero,
 o "Ambos números son negativos" si los dos números son negativos.

'''

numero1 = input('Ingrese un numero')
numero1 = int(numero1)


numero2 = input('Ingrese otro numero')
numero2 = int(numero2)

if numero1 > 0:
    print('El numero 1 es positivo')

if numero2 > 0:
    print('El numero 2 es positivo')

if numero1 < 0 and numero2 <0:
    print('Ambos numeros son negativos')