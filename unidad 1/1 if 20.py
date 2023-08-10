'''
Escribir un programa que le pida al usuario que ingrese dos números enteros,
y luego imprima "Los dos números son iguales" si los dos números son iguales,
"El primer número es mayor" si el primer número es mayor que el segundo,
o "El segundo número es mayor" si el segundo número es mayor que el primero.

'''

numero1 = input('Ingrese un numero ')
numero1 = int(numero1)


numero2 = input('Ingrese otro numero ')
numero2 = int(numero2)

if numero1 > numero2:
    print('El primer número es mayor')
elif numero2 > numero1:
    print('El segundo número es mayor')
else:
    print('Los dos números son iguales')