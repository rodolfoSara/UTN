'''
https://docs.google.com/document/d/1ltL0-vTbhstvgnYgRR2rvLyuZQ-CfoXtPFCA61XJhr4/edit
'''

from data_stark import lista_personajes
menu= '''
1. Imprimir el nombre de supeheroe
2. Mostrar nombre y altura
3. Super más alto
4. Super más bajo
5. Promedio de altura
6. Identidad super heroe más bajo y super más alto
7. super heroe más pesado y más liviano
8. Salir
'''


def imprimir_nombre():
    for nombre in lista_personajes:
        print(f' Nombre {nombre["nombre"]}')

def imprimir_nombre_altura():
    for nombre in lista_personajes:
        print(f' Nombre: {nombre["nombre"]} - Altura: {nombre["altura"]}')

def mas_alto():
    indiceMasAlto = 0
    for i in range(len(lista_personajes)):
        lista_personajes[i]['altura'] = float(lista_personajes[i]['altura'])
        if lista_personajes[i]['altura'] > lista_personajes[indiceMasAlto]['altura']:
            indiceMasAlto = i

    print(f' La altura mayor es {lista_personajes[indiceMasAlto]["altura"]} cm')


def mas_bajo():
    indiceMasBajo=0
    for i in range(len(lista_personajes)):
        if lista_personajes[i]['altura'] < lista_personajes[indiceMasBajo]['altura']:
            indiceMasBajo = i
    print(f' La altura menor es {lista_personajes[indiceMasBajo]["altura"]} cm')

def promedio_altura():
    suma=0
    for i in range(len(lista_personajes)):
        lista_personajes[i]['altura'] = float(lista_personajes[i]['altura'])
        suma+= lista_personajes[i]['altura']

    promedio = suma / i

    print(f'El promedio de altura es {promedio} cm')

def mas_alto_bajo():
    indiceMasAlto = 0
    indiceMasBajo = 0
    for i in range(len(lista_personajes)):
        lista_personajes[i]['altura'] = float(lista_personajes[i]['altura'])
        if lista_personajes[i]['altura'] > lista_personajes[indiceMasAlto]['altura']:
            indiceMasAlto = i
        elif lista_personajes[i]['altura'] < lista_personajes[indiceMasBajo]['altura']:
            indiceMasBajo = i

    print(f' Personaje con altura mayor es {lista_personajes[indiceMasAlto]["nombre"]} : {lista_personajes[indiceMasAlto]["altura"]} cm')
    print(f' Personaje con altura menor es {lista_personajes[indiceMasBajo]["nombre"]} : {lista_personajes[indiceMasBajo]["altura"]} cm')


def mas_Pesado_liviano():
    indiceMasPesado = 0
    indiceMasLiviano = 0
    for i in range(len(lista_personajes)):
        lista_personajes[i]['peso'] = float(lista_personajes[i]['peso'])
        if lista_personajes[i]['peso'] > lista_personajes[indiceMasPesado]['peso']:
            indiceMasPesado = i
        elif lista_personajes[i]['peso'] < lista_personajes[indiceMasLiviano]['peso']:
            indiceMasLiviano = i

    print(f' El peso mayor es {lista_personajes[indiceMasPesado]["peso"]} kg : Personaje: {lista_personajes[indiceMasPesado]["identidad"]}')
    print(f' El peso menor es {lista_personajes[indiceMasLiviano]["peso"]} kg : Personaje: {lista_personajes[indiceMasLiviano]["identidad"]}')

while True:
    print(menu)
    opcion= int(input('Elija una opcion '))
    # uso IF porque no me funciona el match
    if opcion == 1:
        imprimir_nombre()
    elif opcion == 2:
        imprimir_nombre_altura()
    elif opcion == 3:
        mas_alto()
    elif opcion == 4:
        mas_bajo()
    elif opcion == 5:
        promedio_altura()
    elif opcion == 6:
        mas_alto_bajo()
    elif opcion == 7:
        mas_Pesado_liviano()
    elif opcion == 8:
        break

