import json
import re
import csv

with open('dt.json', "r") as archivo:
    lista_jugador = json.load(archivo)

# 1 imprime nombre y posicion de cada jugador
def jugador_posicion(lista:list):
    for i in lista['jugadores']:
        print(f"nombre: {i['nombre']} - Posicion: {i['posicion']}")

#2 muestra nombre y estadisticas de un jugador seleccionado por un indice
def mostar_jugador_por_indice(lista:list, indice: int):
    indice_jugador_dict = {}
    indice_jugador_dict['nombre'] = lista['jugadores'][indice]['nombre']
    indice_jugador_dict['posicion'] = lista['jugadores'][indice]['posicion']
    for k, v in lista['jugadores'][indice]['estadisticas'].items():
        indice_jugador_dict[k] = v

    return indice_jugador_dict

#3 guardar
def generar_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        #recorrer la lista
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11} \n"
            #reemplazar comas y saltos de linea
            mensaje = mensaje.format(video['nombre'].replace(",","-").replace("\n","@"),
                                     video['posicion'].replace(",","-").replace("\n","@"),
                                     video['estadisticas']['temporadas'],
                                     video['estadisticas']['puntos_totales'],
                                     video['estadisticas']['promedio_puntos_por_partido'],
                                     video['estadisticas']['promedio_rebotes_por_partido'],
                                     video['estadisticas']['robos_totales'],
                                     video['estadisticas']['bloqueos_totales'],
                                     video['estadisticas']['porcentaje_tiros_de_campo'],
                                     video['estadisticas']['porcentaje_tiros_libres'],
                                     video['estadisticas']['porcentaje_tiros_triples'],
                                     video["logros"]
                                     )
            archivo.write(mensaje)

'''
Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
Fama del Baloncesto, etc.'''
#4

def buscar_nombre(lista:list, nombre:str):
    es_un_nombre = True
    indice_logros = 0
    # Validar que el nombre tenga el formato deseado
    if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$', nombre):
        print("El nombre ingresado no es válido. Por favor, usa solo letras y espacios.")
        es_un_nombre = False

    if es_un_nombre:
        for i in range(len(lista)):
            if lista['jugadores'][i]['nombre'] == nombre:
                    indice_logros = i
            return indice_logros

'''
5) 
Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
Team, ordenado por nombre de manera ascendente.'''

def promedio(lista:list):
    dic_promedio = {}
    for i in lista['jugadores']:
        dic_promedio[i['nombre']] = i['estadisticas']['promedio_puntos_por_partido']

    return dic_promedio

def crear_lista(dic_promedio:dict):
    list_promedio = []
    for k in dic_promedio.keys():
        list_promedio.append(k)
    return list_promedio

'''
6
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
miembro del Salón de la Fama del Baloncesto.
'''
def miembro_salon_fama(lista:list, nombre):
    for i in lista['jugadores']:
        if i['nombre'] == nombre:
            print(i['logros'][-1])

'''
7
Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
13 Calcular y mostrar el jugador con la mayor cantidad de robos totales.
14) Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
'''
def mayor_cant(lista:dict, mayor:str):
    indice_mayor = 0

    for i in range(len(lista['jugadores'])):
        if lista['jugadores'][i]['estadisticas'][mayor] > lista['jugadores'][indice_mayor]['estadisticas'][mayor]:
            indice_mayor = i

    return indice_mayor

'''
10
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más puntos por partido que ese valor.
11) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más rebotes por partido que ese valor.
12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más asistencias por partido que ese valor.
 15) ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor
18) Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.

'''
def puntos_por_partido(lista:list, estadisticas:str, puntos:float):
    dict_puntos_partido = {}

    for i in lista['jugadores']:
        if i['estadisticas'][estadisticas] > puntos:
            dict_puntos_partido[i['nombre']] = i['estadisticas'][estadisticas]

    return dict_puntos_partido

'''
16) 
Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al
jugador con la menor cantidad de puntos por partido.
'''
def mayor_cant(lista:dict, menor:str):
    indice_menor = 0
    for i in range(len(lista['jugadores'])):
        if lista['jugadores'][i]['estadisticas'][menor] < lista['jugadores'][indice_menor]['estadisticas'][menor]:
            indice_menor = i
    return indice_menor

def promedio_puntos_por_partido(lista:dict, atributo: str):
    suma = 0

    indice_eliminar = mayor_cant(lista, atributo)
    for i in range(len(lista['jugadores'])):
        if i != indice_eliminar:
            suma += lista['jugadores'][i]['estadisticas']['promedio_puntos_por_partido']

    promedio_puntos = suma / (len(lista_jugador['jugadores']) - 1)
    return promedio_puntos



    #print(lista_jugador['jugadores'][0]['estadisticas']['promedio_puntos_por_partido'])

'''
17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
'''

def mayor_cantidad_logros(diccionario:dict):
    mayor_logro = len(diccionario['jugadores'][0]['logros'])
    nombre_mayor_logro = diccionario['jugadores'][0]['nombre']
    dict_mayor_logro = {}
    for i in diccionario['jugadores']:
        if len(i['logros']) > mayor_logro:
            mayor_logro = len(i['logros'])
            nombre_mayor_logro = i['nombre']

    dict_mayor_logro[nombre_mayor_logro] = mayor_logro
    return dict_mayor_logro

'''
20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
ese valor.
'''
def mayor_valor(lista_original: list, clave: str,valor:float) -> list:
    lista = []
    for elemento in lista_original['jugadores']:

        if (elemento['estadisticas'][clave] > valor):
            lista.append(elemento)
    return lista


def quick_sort(lista_original: list, clave, flag_orden: bool)->list:
    lista = lista_original[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while (flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):

            if flag_orden == False and lista[indice_A][clave] < lista[indice_A + 1][clave] \
                    or flag_orden == True and lista[indice_A][clave] > lista[indice_A + 1][clave]:
                lista[indice_A], lista[indice_A + 1] = lista[indice_A + 1], lista[indice_A]
                flag_swap = True

    return lista


'''
21 Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
'''
#ordenar lista
def quick_sort(lista_original: list, clave, flag_orden: bool)->list:
    lista = lista_original['jugadores'][:]
    rango_a = len(lista) - 1
    flag_swap = True

    while (flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if flag_orden == False and lista[indice_A]['estadisticas'][clave] < lista[indice_A + 1]['estadisticas'][clave] \
                    or flag_orden == True and lista[indice_A]['estadisticas'][clave] > lista[indice_A + 1]['estadisticas'][clave]:
                lista[indice_A], lista[indice_A + 1] = lista[indice_A + 1], lista[indice_A]
                flag_swap = True
    return lista

def ranking_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        #recorrer la lista
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4} \n"
            #reemplazar comas y saltos de linea
            mensaje = mensaje.format(video['nombre'].replace(",","-").replace("\n","@"),
                                     video['puntos_totales'],
                                     video['rebotes_totales'],
                                     video['asistencias_totales'],
                                     video['robos_totales']
                                     )
            archivo.write(mensaje)


menu = '''
    1 Mostrar la lista de todos los jugadores del Dream Team.
    2 Introducir un indice y ver nombre y estadistica del jugador
    3 Guardar la estadística del jugador a csv
    4 buscar por nombre y ver sus logros
    5 Mostrar promedio de puntos por partido ordenados por nombre
    6 buscar por nombre si esta en el salon de la fama
    7 jugador con mayor cantidad de rebotes
    8 jugador con mayor porcentaje_tiros_de_campo
    9 El jugador con mayora sistencias
    10 Puntos por partido
    11 Promedio rebotes por partido
    12 Promedio asistencias por partido
    13 Calcular y mostrar el jugador con la mayor cantidad de robos totales
    14 Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
    15 ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor
    16 Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad
    17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    18 ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor
    19 Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
    20 porcentaje de tiros de campo superior a ese valor
    21 Ranking de cada jugador
'''




while True:
    print(menu)
    respuesta = input('Seleccione un número ')
    respuesta = int(respuesta)

    match respuesta:
        case 1:
            jugador_posicion(lista_jugador)

        case 2:
            indice = input('Seleccione un indice ')
            indice = int(indice)
            print(lista_jugador['jugadores'][indice]['nombre'])
            estadistica_de_un_jugador = []
            estadistica_de_un_jugador.append(lista_jugador['jugadores'][indice])
            print(estadistica_de_un_jugador)

        case 3:
            guardar_estadisticas = input('Quiere guardar la estádisticas si / no ')
            guardar_estadisticas.lower()
            # valido respuesta
            while guardar_estadisticas != 'si' and guardar_estadisticas != 'no':
                guardar_estadisticas = input('Quiere guardar la estádisticas si / no ')
            if guardar_estadisticas == 'si':
                try:
                    generar_csv('estadistica_jugador.csv', estadistica_de_un_jugador)
                    print('se ha guardado exitosamente')
                except:
                    print('Ha ocurrido un error')

        case 4:
            nombre = input('Ver logros - Escriba el nombre del jugador ')
            indice = buscar_nombre(lista_jugador, nombre)
            print(lista_jugador['jugadores'][indice]['logros'])

        case 5:
            diccionario = (promedio(lista_jugador))
            lista = crear_lista(diccionario)
            lista_ordenada = sort(lista, True)
            diccionario_ordenado = {}
            for i in lista_ordenada:
                diccionario_ordenado[i] = diccionario[i]
            print(diccionario_ordenado)

        case 6:
            nombre = input('Escriba el nombre ')
            miembro_salon_fama(lista_jugador, nombre)

        case 7:
            indice_mayor_rebotes =  mayor_cant(lista_jugador, 'rebotes_totales')
            print(f'El jugador con mayor cantidad de rebotes {lista_jugador["jugadores"][indice_mayor_rebotes]["nombre"]}')

        case 8:
            indice_mayor_tiros = mayor_cant(lista_jugador, 'porcentaje_tiros_de_campo')
            print(f'El jugador con mayor porcentaje_tiros_de_campo {lista_jugador["jugadores"][indice_mayor_tiros]["nombre"]}')

        case 9:
            indice_mayor = mayor_cant(lista_jugador, 'asistencias_totales')
            print(f'El jugador con mayor sistencias {lista_jugador["jugadores"][indice_mayor]["nombre"]}')

        case 10:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',','.')
            try:
                puntos = float(puntos)
                print(puntos_por_partido(lista_jugador, 'promedio_puntos_por_partido', puntos))
            except:
                print('escriba un numero con decimales o entero')


        case 11:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',', '.')
            try:
                puntos = float(puntos)
                print(puntos_por_partido(lista_jugador, 'promedio_rebotes_por_partido', puntos))
            except:
                print('escriba un numero con decimales o entero')



        case 12:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',', '.')
            try:
                puntos = float(puntos)
                print(puntos_por_partido(lista_jugador, 'promedio_asistencias_por_partido', puntos))
            except:
                print('escriba un numero con decimales o entero')

        case 13:
            indice_mayor = mayor_cant(lista_jugador, 'robos_totales')
            print(f'El jugador con mayor cant de rebotes {lista_jugador["jugadores"][indice_mayor]["nombre"]} con cant de rebotes: {lista_jugador["jugadores"][indice_mayor]["estadisticas"]["robos_totales"]}')

        case 14:
            indice_mayor = mayor_cant(lista_jugador, 'bloqueos_totales')
            print(f'El jugador con mayor {lista_jugador["jugadores"][indice_mayor]["nombre"]} con cant de bloqueos: {lista_jugador["jugadores"][indice_mayor]["estadisticas"]["robos_totales"]}')

        case 15:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',', '.')
            try:
                puntos = float(puntos)
                print(puntos_por_partido(lista_jugador, 'porcentaje_tiros_libres', puntos))
            except:
                print('escriba un numero con decimales o entero')

        case 16:
            promedio_puntos = promedio_puntos_por_partido(lista_jugador, 'promedio_puntos_por_partido')
            promedio_puntos = round(promedio_puntos,2)
            print(f'El promedio de puntos, excepto el jugador con menos puntos es {promedio_puntos}')

        case 17:
            print(mayor_cantidad_logros(lista_jugador))

        case 18:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',', '.')
            try:
                puntos = float(puntos)
                print(puntos_por_partido(lista_jugador, 'porcentaje_tiros_triples', puntos))
            except:
                print('escriba un numero con decimales o entero')

        case 19:
            indice_mayor = mayor_cant(lista_jugador, 'temporadas')
            print(f'El jugador con mayor  temporadas {lista_jugador["jugadores"][indice_mayor]["nombre"]} con: {lista_jugador["jugadores"][indice_mayor]["estadisticas"]["temporadas"]}')

        case 20:
            puntos = input('Escriba número ')
            puntos = puntos.replace(',', '.')
            try:
                puntos = float(puntos)
                mayor_al_valor = mayor_valor(lista_jugador, 'porcentaje_tiros_de_campo', puntos)
            except:
                print('escriba un numero con decimales o entero')

            lista_ordenada = quick_sort(mayor_al_valor, 'posicion', True)
            for i in lista_ordenada:
                print(i)

        case 21:
            #porcentaje_tiros_de_campo
            puntos = quick_sort(lista_jugador, 'puntos_totales', False)
            ranking = [{'nombre': puntos[i]['nombre'], 'puntos_totales': i + 1}for i in range(len(puntos))]


            rebotes = quick_sort(lista_jugador, 'rebotes_totales', False)
            print(rebotes)
            for i in ranking:
                for j in range(len(rebotes)):
                    if i['nombre'] == rebotes[j]['nombre']:
                        i['rebotes_totales'] = j + 1

            asitencias = quick_sort(lista_jugador, 'asistencias_totales', False)
            print(asitencias)
            for i in ranking:
                for j in range(len(asitencias)):
                    if i['nombre'] == asitencias[j]['nombre']:
                        i['asistencias_totales'] = j + 1

            robos = quick_sort(lista_jugador, 'robos_totales', False)
            print(robos)
            for i in ranking:
                for j in range(len(robos)):
                    if i['nombre'] == robos[j]['nombre']:
                        i['robos_totales'] = j + 1

            ranking_csv('ranking.csv', ranking)























            '''puntos_totales
            rebotes_totales
            asistencias_totales
            robos_totales'''
            
























