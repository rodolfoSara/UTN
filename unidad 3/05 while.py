'''
Dado un número entero n, imprimir si el número es primo o no.
'''

num = input('Escriba un numero ')
num = int(num)


for numero in range(1,num):
    print(numero)
    if num % numero  == 0:
        print('si')





