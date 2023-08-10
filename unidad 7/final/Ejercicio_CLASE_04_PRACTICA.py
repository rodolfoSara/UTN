from data_stark import lista_personajes

menu='''
1 nombre de cada superhéroe de género M
2 nombre de cada superhéroe de género F
3 superhéroe más alto de género M
4 superhéroe más alto de género F
5 superhéroe más bajo de género M
6 superhéroe más bajo de género F
7 altura promedio de los superhéroes de género M
8 altura promedio de los superhéroes de género F
9 Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
10 cuántos superhéroes tienen cada tipo de color de ojos
11 cuántos superhéroes tienen cada tipo de color de pelo
12 cuántos superhéroes tienen cada tipo de inteligencia
13 Listar todos los superhéroes agrupados por color de ojos
14 Listar todos los superhéroes agrupados por color de pelo
15 Listar todos los superhéroes agrupados por tipo de inteligencia
'''
#castear
for i in lista_personajes:
    i['altura'] = float(i['altura'])
    print(i['nombre'], i['altura'])

'''
1 nombre de cada superhéroe de género M
2 nombre de cada superhéroe de género F
'''
def nombre(lista_personajes:list, genero:str):
    for i in lista_personajes:
        if i['genero'] == genero:
            print(i['nombre'])

'''
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
'''
def altura_mayor_menor(lista_personajes, genero:str, mayor:bool):
    indice = 0
    for i in range(len(lista_personajes)):
        if lista_personajes[i]['genero'] == genero:
            if mayor:
                if lista_personajes[i]['altura'] > lista_personajes[indice]['altura']:
                    indice = i
            elif mayor == False:
                if lista_personajes[i]['altura'] < lista_personajes[indice]['altura']:
                    indice = i
    return indice

'''
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
'''
def promedio(lista_personajes, genero):
    suma = 0
    cantidad = 0
    for i in lista_personajes:
        if i['genero'] == genero:
            suma =+ i['altura']
            cantidad += 1
    print(suma)
    promedio = suma / cantidad
    return promedio


'''
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
'''
def contar_atributos(lista_personajes, atributo):
    atributo_dict={}
    atributo_dict['No tiene'] = 0
    for i in lista_personajes:
        if i[atributo] in atributo_dict:
            atributo_dict[i[atributo]] +=1
        elif i['inteligencia'] == "":
            atributo_dict['No tiene'] +=1
        else:
            atributo_dict[i[atributo]] = 1

    return atributo_dict

'''
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
'''
def agrupar_atributos(lista_personajes, atributo):
    # Creamos un diccionario donde cada clave puede tener múltiples valores almacenados en una lista
    diccionario_con_valores_multiples = {}
    diccionario_con_valores_multiples['No tiene']= 0

    # Iteramos sobre los elementos del diccionario original y agregamos las claves y valores al diccionario nuevo
    for i in range(len(lista_personajes)):
        for clave, valor in lista_personajes[i].items():
            if clave == atributo:
                # Si la clave ya existe en el diccionario nuevo, simplemente agregamos el valor a la lista
                if valor in diccionario_con_valores_multiples:
                    diccionario_con_valores_multiples[valor].append(lista_personajes[i]['nombre'])
                #si valor es 0 sumamos 1
                elif valor == '':
                    diccionario_con_valores_multiples['No tiene'] += 1
                # Si la clave no existe, creamos una nueva lista con el valor como primer elemento
                else:
                    diccionario_con_valores_multiples[valor] = [lista_personajes[i]['nombre']]
    return diccionario_con_valores_multiples

while True:
    print(menu)
    option = int(input('Seleccione una opción '))
    match(option):
        case 1:
            nombre(lista_personajes, 'M')
        case 2:
            nombre(lista_personajes, 'F')
        case 3:
            indice = altura_mayor_menor(lista_personajes, 'M', True)
            print(f"El heroe Masculino más alto es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")
        case 4:
            indice = altura_mayor_menor(lista_personajes, 'F', True)
            print(f"El heroe Femenino más alto es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")
        case 5:
            indice = altura_mayor_menor(lista_personajes, 'M', False)
            print(f"El heroe Masculino más bajo es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")
        case 6:
            indice = altura_mayor_menor(lista_personajes, 'F', False)
            print(f"El heroe femenino más bajo es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")

        case 7:
            print(f"El promedio de altura masculino {round(promedio(lista_personajes, 'M'), 2)}")

        case 8:
            print(f"El promedio de altura masculino {round(promedio(lista_personajes, 'F'), 2)}")

        case 9:
            indice = altura_mayor_menor(lista_personajes, 'M', True)
            print(f"El heroe Masculino más alto es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")

            indice = altura_mayor_menor(lista_personajes, 'F', True)
            print(f"El heroe Femenino más alto es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")

            indice = altura_mayor_menor(lista_personajes, 'M', False)
            print(f"El heroe Masculino más bajo es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")

            indice = altura_mayor_menor(lista_personajes, 'F', False)
            print(f"El heroe femenino más bajo es {lista_personajes[indice]['nombre']} "
                  f"con una altura de {lista_personajes[indice]['altura']}")
        case 10:
            print(f"cantidad de color de ojos {contar_atributos(lista_personajes, 'color_ojos')}")

        case 11:
            print(f"cantidad de color de pelo {contar_atributos(lista_personajes, 'color_pelo')}")

        case 12:
            print(f"cantidad de tipo de inteligencia {contar_atributos(lista_personajes, 'inteligencia')}")

        case 13:
            argupado = agrupar_atributos(lista_personajes, "color_ojos")
            print(f'Los herores agrupado por colo de ojo {argupado}')
        case 14:
            argupado = agrupar_atributos(lista_personajes, "color_pelo")
            print(f'Los herores agrupado por colo de pelo {argupado}')
        case 15:
            argupado = agrupar_atributos(lista_personajes, "inteligencia")
            print(f'Los herores agrupado por inteligencia {argupado}')

