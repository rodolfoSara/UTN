'''
Dado un número entero n, imprimir todos los números primos menores o iguales a n.
'''

num = input('escriba un numero ')
num = int(num)

i=0
j=0

def es_primo(num):
    print(num)
    for numero in range(1, num):
        if num % numero == 0:
            return False
    return True

resultado = es_primo(num)
print(resultado)
