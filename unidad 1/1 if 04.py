'''Escribir un programa que le pida al usuario que ingrese dos números enteros,
 y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo,
   "El segundo número es mayor" si el segundo número es mayor que el primero,
     o "Los dos números son iguales" si los dos números son iguales.
'''
numero1 = input('Ingrese un numero')
numero1 = int(numero1)

numero2 = input('Ingrese un numero')
numero2 = int(numero2)

if numero1 > numero2:
    print('Numero 1 es mayor')
elif numero2 > numero1:
    print('Numero 2 es mayor')
else:
    print('Numero son iguales')