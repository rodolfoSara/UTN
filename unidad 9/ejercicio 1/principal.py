'''
Castear datos
'''
def castear_datos_float(lista_heroes:list, atributo:str):
    indice_no_casteados = []
    for dato in range(len(lista_heroes)):
        if lista_heroes[dato][atributo] != float and lista_heroes[dato][atributo].replace('.', '').isnumeric():
            lista_heroes[dato][atributo] = float(lista_heroes[dato][atributo])
        else:
            indice_no_casteados.append(dato)

    if len(indice_no_casteados) > 0:
        print(f"Los indices {atributo} que no se pudieron convertir a numero son {indice_no_casteados}")
    else:
        print(f'Todos los datos {atributo} fueron correctamente casteados')

def castear_datos_int(lista_heroes:list, atributo:str):
    indice_no_casteados = []
    for dato in range(len(lista_heroes)):
        if lista_heroes[dato][atributo] != float and lista_heroes[dato][atributo].isnumeric():
            lista_heroes[dato][atributo] = float(lista_heroes[dato][atributo])
        else:
            indice_no_casteados.append(dato)

    if len(indice_no_casteados) > 0:
        print(f"Los indices de {atributo} que no se pudieron convertir a numero son {indice_no_casteados}")
    else:
        print(f'Todos los datos {atributo} fueron correctamente casteados')







'''
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
'''

def imprimir_nombre(lista_heroes:list, genero:str):
    for heroes in lista_heroes:
        if heroes['genero'] == genero:
            print(heroes['nombre'])

'''
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
'''
def altura_heroes(lista_heroes:list, genero:str, mas_alto:bool) -> int:
    indice = 0
    for heroes in range(len(lista_heroes)):
        if mas_alto:
            if lista_heroes[heroes]['genero'] == genero:
                if lista_heroes[heroes]['altura'] > lista_heroes[indice]['altura']:
                    indice = heroes
        elif mas_alto == False:
            if lista_heroes[heroes]['genero'] == genero:
                if lista_heroes[heroes]['altura'] < lista_heroes[indice]['altura']:
                    indice = heroe
    return indice

'''
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
'''
def promedio_altura_heroes(lista_heroes:list, genero:str) -> float:
    suma = 0
    for heroes in lista_heroes:
        if heroes['genero'] == genero:
            suma += heroes['altura']
    promedio = round(suma / len(lista_heroes), 2)

    return promedio

'''
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
'''
def contar_atributos(lista_heroes:list, atributo:str) -> dict:
    dict_contar_atributos ={}
    dict_contar_atributos['No tiene'] = 0
    for heroes in lista_heroes:
        if heroes[atributo] == "":
            dict_contar_atributos['No tiene'] += 1
        elif heroes[atributo] in dict_contar_atributos:
            dict_contar_atributos[heroes[atributo]] += 1
        else:
            dict_contar_atributos[heroes[atributo]] = 1
    return dict_contar_atributos

'''
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
'''
def agrupar_atributos(lista_heroes:dict, atributo:str) -> dict:
    dict_agrupar_atributos = {}
    dict_agrupar_atributos['No tiene'] = []
    for heroes in range(len(lista_heroes)):
        for key, value in lista_heroes[heroes].items():
            if key == atributo:
                if value in dict_agrupar_atributos:
                    dict_agrupar_atributos[value].append(lista_heroes[heroes]['nombre'])
                elif value == "":
                    dict_agrupar_atributos['No tiene'].append(lista_heroes[heroes]['nombre'])
                else:
                    dict_agrupar_atributos[value] = [lista_heroes[heroes]['nombre']]
    return dict_agrupar_atributos
