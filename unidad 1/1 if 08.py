'''

Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto,
 o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.

'''

def es_cuadrado_perfecto(numero):
    # Obtenemos la raíz cuadrada del número
    raiz_cuadrada = numero ** 0.5

    # Verificamos si la raíz cuadrada es un número entero
    if int(raiz_cuadrada) ** 2 == numero:
        return True
    else:
        return False

try:
    # Solicitamos al usuario que ingrese un número entero positivo
    numero_ingresado = int(input("Ingrese un número entero positivo: "))

    if numero_ingresado > 0:
        if es_cuadrado_perfecto(numero_ingresado):
            print("El número es un cuadrado perfecto.")
        else:
            print("El número no es un cuadrado perfecto.")
    else:
        print("Por favor, ingrese un número entero positivo.")
except ValueError:
    print("Error: Debe ingresar un número entero.")
