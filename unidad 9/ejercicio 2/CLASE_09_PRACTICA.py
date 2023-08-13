import json


def abrir_json(ruta:str) -> json:
    with open(ruta) as f:
        lista_heroes = json.load(f)
        return lista_heroes['heroes']

lista_heroes = abrir_json('data_stark_archivos.json')

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
        if lista_heroes[dato][atributo] != int and lista_heroes[dato][atributo].isnumeric():
            lista_heroes[dato][atributo] = int(lista_heroes[dato][atributo])
        else:
            indice_no_casteados.append(dato)

    if len(indice_no_casteados) > 0:
        print(f"Los indices de {atributo} que no se pudieron convertir a numero son {indice_no_casteados}")
    else:
        print(f'Todos los datos {atributo} fueron correctamente casteados')

def ordenar_y_listar_por_clave(lista_original: list, clave: str, menor_a_mayor:bool) -> list:

    lista_de = []
    lista_iz = []

    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0][clave]
        for elemento in lista_original[1:]:
            if menor_a_mayor == True:
                if (elemento[clave] < pivot):
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
            elif menor_a_mayor == False:
                if (elemento[clave] > pivot):
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)


    lista_iz = ordenar_y_listar_por_clave(lista_iz, clave, menor_a_mayor)
    lista_iz.append(lista_original[0])
    lista_de = ordenar_y_listar_por_clave(lista_de, clave, menor_a_mayor)
    lista_iz.extend(lista_de)
    return lista_iz


def quick_sort(lista_original: list, clave, flag_orden: bool)->list:
    lista = lista_original[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while (flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if flag_orden == False and len(lista[indice_A][clave]) < len(lista[indice_A + 1][clave]) \
                    or flag_orden == True and len(lista[indice_A][clave]) > len(lista[indice_A + 1][clave]):
                lista[indice_A], lista[indice_A + 1] = lista[indice_A + 1], lista[indice_A]
                flag_swap = True
    return lista


castear_datos_float(lista_heroes, 'altura')
castear_datos_float(lista_heroes, 'peso')
castear_datos_int(lista_heroes, 'fuerza')

'''
for i in lista_heroes:
    print(i)
'''
menu ='''
    1 ordenar por altura
    2 Ordenar por peso
    3 Ordenar por nombre
    4 Ordenar por longitud de nombre
    
    '''



while True:
    print(menu)
    option = int(input('Elija una opción '))

    match(option):
        case 1:
            ordenada_por_altura = ordenar_y_listar_por_clave(lista_heroes, 'altura', True)
            for i in ordenada_por_altura:
                print(i)
        case 2:
            ordenada_por_peso = ordenar_y_listar_por_clave(lista_heroes, 'peso', True)
            for i in ordenada_por_peso:
                print(i)
        case 3:
            ordenada_por_nombre = ordenar_y_listar_por_clave(lista_heroes, 'nombre', True)
            for i in ordenada_por_nombre:
                print(i)
        case 3:
            ordenada_por_altura = ordenar_y_listar_por_clave(lista_heroes, 'nombre', True)
            for i in ordenada_por_altura:
                print(i)
        case 4:
            ordenada_por_largo_nombre = quick_sort(lista_heroes, 'nombre', False)
            for i in ordenada_por_largo_nombre:
                print(i)



