from data_stark import lista_personajes

menu= '''
    1 Imprimir nombre
    2 Imprimir nombre y altura
    3 Superhéroe más alto
    4 Superhéroe más bajo
    5 Promedio aLtura de superheroes
    6 identidad del heroe más alto y más bajo
    7 Heroe mas pesado y más liviano
    8 Salir
'''
#casteo
for i in lista_personajes:
   i['altura'] = float(i['altura'])
   i['peso'] = float(i['peso'])


'''
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
'''
def imprimir(lista_personajes, altura=False):
    for i in lista_personajes:
        if altura == False:
            print(f"El nombre es {i['nombre']}")
        else:
            print(f"El nombre es {i['nombre']} y la Altura {round(i['altura'], 2)} ")

'''
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
G. Informar cual es la identidad del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
'''
def min_max(lista_personajes, atributo, max= True):
    indice = 0
    for i in range(len(lista_personajes)):
        if max:
            if lista_personajes[i][atributo] >  lista_personajes[indice][atributo]:
                indice = i
        else:
            if lista_personajes[i][atributo] <  lista_personajes[indice][atributo]:
                indice = i
    return indice

'''
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
'''
def promedio(lista_personajes):
    suma = 0
    for i in lista_personajes:
        suma += i['altura']
    promedioAltura = suma / len(lista_personajes)
    return promedioAltura


while True:
    print(menu)
    option = int(input('Seleccione una opción '))

    match(option):
        case 1:
            imprimir(lista_personajes, altura=False)

        case 2:
            imprimir(lista_personajes, True)
        case 3:
            indice = min_max(lista_personajes,  'altura' , True)
            print(f"El heroe más alto es {lista_personajes[indice]['nombre']} con una altura de {lista_personajes[indice]['altura']}")
        case 4:
            indice = min_max(lista_personajes,  'altura' , False)
            print(f"El heroe más bajo es {lista_personajes[indice]['nombre']} con una altura de {lista_personajes[indice]['altura']}")
        case 5:
            print(f"El promedio de altura de los superheroes es {round(promedio(lista_personajes), 2)}")
        case 6:
            indice = min_max(lista_personajes, 'altura', True)
            print(f"La identidad del heroe más alto es {lista_personajes[indice]['identidad']}")
            indice = min_max(lista_personajes, 'altura', False)
            print(f"La identidad del heroe más bajo es {lista_personajes[indice]['identidad']}")
        case 7:
            indice = min_max(lista_personajes, 'peso', True)
            print(f"El heroe más pesado es {lista_personajes[indice]['nombre']} con una altura de {lista_personajes[indice]['peso']}")

            indice = min_max(lista_personajes, 'peso', False)
            print(f"El heroe más bajo es {lista_personajes[indice]['nombre']} con una altura de {lista_personajes[indice]['peso']}")
        case 8:
            break