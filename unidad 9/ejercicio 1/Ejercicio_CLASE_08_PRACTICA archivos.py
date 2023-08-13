import json
import re
from principal import *
from parte1 import *
from parte2 import *

castear_datos_float(lista_heroes, 'altura')
castear_datos_float(lista_heroes, 'peso')
castear_datos_int(lista_heroes, 'fuerza')

for i in lista_heroes:
    print(i)


while True:
    imprimir_menu()
    option = input('Selecciones una opción ')
    while not validar_opcion_menu(option):
        option = input('Ingrese una opción válida ')
        validar_opcion_menu(option)
    option = option.upper()

    match(option):
        case 'A':
            imprimir_nombre(lista_heroes, 'M')
        case 'B':
            imprimir_nombre(lista_heroes, 'F')
        case 'C':
            indice = altura_heroes(lista_heroes, 'M', True)
            print(f"El nombre del heroe masculino más alto: {lista_heroes[indice]['nombre']}")
        case 'D':
            indice = altura_heroes(lista_heroes, 'F', True)
            print(f"El nombre del heroe femenino más alta: {lista_heroes[indice]['nombre']}")
        case 'E':
            indice = altura_heroes(lista_heroes, 'M', False)
            print(f"El nombre del heroe masculino más bajo: {lista_heroes[indice]['nombre']}")
        case 'F':
            indice = altura_heroes(lista_heroes, 'F', False)
            print(f"El nombre del heroe femenino más baja: {lista_heroes[indice]['nombre']}")
        case 'G':
            print(f"La altura promedio de hombres es: {promedio_altura_heroes(lista_heroes, 'M')}")
        case 'H':
            print(f"La altura promedio de mujeres es: {promedio_altura_heroes(lista_heroes, 'F')}")
        case 'I':

            indice = altura_heroes(lista_heroes, 'M', True)
            print(f"El nombre del heroe masculino más alto: {lista_heroes[indice]['nombre']}")

            indice = altura_heroes(lista_heroes, 'F', True)
            print(f"El nombre del heroe femenino más alta: {lista_heroes[indice]['nombre']}")

            indice = altura_heroes(lista_heroes, 'M', False)
            print(f"El nombre del heroe masculino más bajo: {lista_heroes[indice]['nombre']}")

            indice = altura_heroes(lista_heroes, 'F', False)
            print(f"El nombre del heroe femenino más baja: {lista_heroes[indice]['nombre']}")
        case 'J':
            print(f"Agrupados por color de ojos: {contar_atributos(lista_heroes, 'color_ojos')}")
        case 'K':
            print(f"Agrupados por color de pelo: {contar_atributos(lista_heroes, 'color_pelo')}")
        case 'L':
            print(f"Agrupados por color de Inteligencia: {contar_atributos(lista_heroes, 'inteligencia')}")
        case 'M':
            print(f"Agrupar por color de ojos: {agrupar_atributos(lista_heroes, 'color_ojos')}")
        case 'N':
            print(f"Agrupar por color de pelo: {agrupar_atributos(lista_heroes, 'color_pelo')}")
        case 'O':
            print(f"Agrupar por inteligencia: {agrupar_atributos(lista_heroes, 'inteligencia')}")
        case 'P':
            nombre_archivo = 'archivo.csv'
            contenido = "Nombre,Edad,Ciudad\nJuan,30,Barcelona\nMaría,25,Madrid\nCarlos,35,Sevilla"

            #nombre_archivo = input('Escriba el nombre del archivo y su extensión ')
            #contenido = input('Escriba el contenido a guardar ')
            resultado = guardar_archivo(nombre_archivo, contenido)
            print(resultado)
        case 'Q':
            #ruta_archivo = input('Escriba el nombre del archivo ')
            #eer_archivo_guardado(ruta_archivo)
            pass
        case 'R':
            cadena = input('Escriba la cadena a capitalizar ')
            print(capitalizar_palabras(cadena))
        case 'S':
            cadena = input('Escriba el nombre a capitalizar ')
            print(f"Nombre: {capitalizar_palabras(cadena)}")
        case 'T':
            nombre = input('Escriba el nombre del heroe ')
            key = input('Escriba el atributo que quiere saber ')
            print(obtener_nombre_y_dato(lista_heroes, nombre, key))
        #PARTE 2
        case 'U':

            menu_parte2='''
                1 confirmar el genero del personaje
                2 Guardar personajes de genero elegido
            '''
            print(menu_parte2)
            option_parte2 = int(input(' Elija un opción '))
            match(option_parte2):
                case 1:
                    nombre = input('Seleccione el nombre ')
                    genero = input('Seleccione el genero M o F ')
                    print(f" Es genero {genero}: {es_genero(lista_heroes, nombre, genero)}")
                case 2:
                    genero = input('Escriba un genero F o M ')
                    lista_genero = lista_genero_func(lista_heroes, genero)
                    lista_genero = capitalizar_palabras(lista_genero)
                    print(f"Los heroes son de genero: {genero} y sus nombres son: {lista_genero} ")

                    nombre_archivo = input('Escriba el nombre con el que quiere guardar el archivo y extensión ')
                    guardar_archivo(nombre_archivo, lista_genero)
