import json
import re


def abrir_json(ruta:str) -> json:
    with open(ruta) as f:
        lista_heroes = json.load(f)
        return lista_heroes['heroes']

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

#ordenar lista
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


def validar_asc_sec(ordenar:str):
    comprobar = re.search("(asc|desc)[endente]?", ordenar)
    if comprobar:
        return True
    return False

def validar_float_int(atributo:str):
    if float(lista_heroes[0][atributo]):
        return True
    elif int((lista_heroes[0][atributo])):
        return True
    return False

def promediar(lista_heroes:list, atributo:str):
    suma = 0
    promedio = 0
    for i in lista_heroes:
        suma += i[atributo]
    promedio = suma / len(lista_heroes)
    return promedio

def validar_mayor(valor:str):
    if valor != 'mayor' and valor != 'menor':
        return False
    return True

def lista_mayor_menor_a_promedio(lista_original: list, clave: str, mayor:bool, promedio:float) -> list:
    lista = []
    for elemento in lista_original:
        if mayor == True:
            if (elemento[clave] > promedio):
                lista.append(elemento)
        elif mayor == False:
            if (elemento[clave] < promedio):
                lista.append(elemento)
    return lista

def validar_inteligencia(inteligencia:str):
    inteligencia = re.search("(good|average|high)", inteligencia, re.IGNORECASE)
    if inteligencia:
        return True
    return False

def agrupar_por_inteligencia(lista_original: list, valor: str) -> list:
    lista = []
    for i in lista_original:
        if i['inteligencia']  == valor:
           lista.append(i)
    return lista

def generar_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo, 'w') as archivo:
        #recorrer la lista
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4},{5} \n"
            #reemplazar comas y saltos de linea
            mensaje = mensaje.format(video['nombre'].replace(",","-").replace("\n","@"),
                                     video['identidad'].replace(",","-").replace("\n","@"),
                                     video['empresa'].replace(",","-").replace("\n","@"),
                                     video['altura'],
                                     video['peso'],
                                     video['genero'].replace(",","-").replace("\n","@"),
                                     video['color_ojos'].replace(",","-").replace("\n","@"),
                                     video['color_pelo'].replace(",","-").replace("\n","@"),
                                     video['fuerza'],
                                     video['inteligencia'].replace(",","-").replace("\n","@"))
            archivo.write(mensaje)

lista_heroes = abrir_json('data_stark_archivos.json')
castear_datos_float(lista_heroes,'altura')
castear_datos_float(lista_heroes,'peso')
castear_datos_int(lista_heroes, 'fuerza')



menu = '''
    1 Listar los primeros N héroes
    2 Ordenar y Listar héroes por altura.
    3 Ordenar y Listar héroes por fuerza.
    4. Calcular promedio de cualquier key numérica
    5 Buscar héroes por inteligencia [good, average, high]
    6 Guardar
    '''

while True:
    print(menu)
    option = int(input('Ingrese una opción '))
    match (option):
        case 1:
            numero = int(input('Ingrese la cantidad de heroes que quiere ver '))
            n_heroes = []
            while numero < 1 or numero > len(lista_heroes):
                numero = int(input(f'Ingrese una cantidad entre 0 y {len(lista_heroes)}  '))
            for i in range(len(lista_heroes)):
                if i < numero:
                    print(lista_heroes[i])
                    n_heroes.append(lista_heroes[i])
        case 2:
            ordenar = input('Quiere ordenar de manera ascendente o descendente ')
            while validar_asc_sec(ordenar) != True:
                ordenar = input('Quiere ordenar de manera ascendente o descendente ')
            if ordenar == 'asc' or ordenar == 'ascendente':
                lista_ordenada_altura = ordenar_y_listar_por_clave(lista_heroes, 'altura', False)
            else:
                lista_ordenada_altura = ordenar_y_listar_por_clave(lista_heroes, 'altura', True)

            for i in lista_ordenada_altura:
                print(i)
        case 3:
            ordenar = input('Quiere ordenar de manera ascendente o descendente ')
            while validar_asc_sec(ordenar) != True:
                ordenar = input('Quiere ordenar de manera ascendente o descendente ')
            if ordenar == 'asc' or ordenar == 'ascendente':
                ordenada_por_fuerza = ordenar_y_listar_por_clave(lista_heroes, 'fuerza', False)
            else:
                ordenada_por_fuerza = ordenar_y_listar_por_clave(lista_heroes, 'fuerza', True)

            for i in ordenada_por_fuerza:
                print(i)
        case 4:
            atributo = input('Escriba la clave a promediar ')
            es_num = validar_float_int(atributo)
            while es_num == False:
                print('No se puede promediar ')
                atributo = input('Escriba la clave a promediar ')

            promedio = round(promediar(lista_heroes, atributo), 2)
            print(f'El promedio  de {atributo} es {promedio}')

            mayor = input('mayor o menor al promedio')
            mayor = mayor.lower()
            while validar_mayor(mayor) == False:
                mayor = input('mayor o menor')
            if mayor == 'mayor':
                mayor = True
            else:
                mayor = False

            lista_promedio = lista_mayor_menor_a_promedio(lista_heroes, atributo, mayor, promedio)
            for i in lista_promedio:
                print(i)
        case 5:
            inteligencia = input('Seleccione tipo de inteligencia [good, average, high] ')
            es_inteligencia = validar_inteligencia(inteligencia)

            while es_inteligencia == False:
                inteligencia = input('Seleccione tipo de inteligencia [good, average, high] ')
                es_inteligencia = validar_inteligencia(inteligencia)

            inteligencia = inteligencia.lower()

            agrupar_inteligencia = agrupar_por_inteligencia(lista_heroes, inteligencia)
            for i in agrupar_inteligencia:
                print(i)
        case 6:
            menu_guardar = '''
                A Guardar sólo N cantidad de heroes
                B Guardar ordenados por altura
                C Guardar ordenados por fuerza
                D Guardar por el mayor o menos al promedio de un atributo '''
            print(menu_guardar)
            opcion_guardar = input('Selecciones como quiere guardar ')

            match opcion_guardar:
                case 'A':
                    try:
                        generar_csv('cantidad_data_bzrp.csv', n_heroes)
                    except:
                        print('Seleccionó primero: 1 Listar los primeros N héroes ')
                case 'B':
                    try:
                        generar_csv('ordenada_por_altura.csv', lista_ordenada_altura)
                    except:
                        print('Seleccionó primero: 2 ordenar por altura ')
                case 'C':
                    try:
                        generar_csv('ordenada_por_fuerza.csv', ordenada_por_fuerza)
                    except:
                        print('Seleccionó primero: 3 ordenar por fuerza ')

                case 'D':
                    try:
                        generar_csv('ordenada_por_promedio.csv', lista_promedio)
                    except:
                        print('Seleccionó primero: 3 ordenar por fuerza ')



























            #ordenar_y_listar_por_clave(lista_original: list, clave: str, menor_a_mayor: bool)