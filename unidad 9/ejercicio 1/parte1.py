import json
import re

#1. Primera Parte
def imprimir_menu():
    menu = '''
    A. imprimir género M
    B. imprimir género F
    C. Más alto de género M
    D. Más alto de género F
    E. Más bajo de género M
    F. Más bajo de género F
    G. Altura promedio de los superhéroes de género M
    H. Altura promedio de los superhéroes de género F
    I. Nombre del superhéroe de los indicadores anteriores (ítems C a F)
    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    L. Cada tipo de inteligencia
    M. Listar todos los superhéroes agrupados por color de ojos.
    N. Listar todos los superhéroes agrupados por color de pelo.
    O. Listar todos los superhéroes agrupados por tipo de inteligencia
    P. Guardar Cadena
    Q. Leer archivo guardado REVEER
    R. Capitalizar una cadena
    U. Parte 2
    Z. Salir
    '''
    print(menu)


def validar_opcion_menu(option:str):
    if len(option) > 1:
        return False
    patron = r"[a-zA-Z]"
    resultado = re.search(patron, option)
    if resultado:
        return True
    else:
        return False

def abrir_json(ruta:str) -> json:
    with open(ruta) as f:
        lista_heroes = json.load(f)
        return lista_heroes['heroes']


lista_heroes = abrir_json('data_stark_archivos.json')

def guardar_archivo(nombre_archivo:str, contenido:str) -> bool:
    try:
        with open(nombre_archivo, 'w+') as file:
            json.dump(contenido, file, indent=4, ensure_ascii=False)
        return True
    except:
        return False

'''
#lee el archivo guardado
def leer_archivo_guardado(ruta_archivo:str):
    with open(ruta_archivo) as f:
        lista_heroes = json.load(f)
        return lista_heroes
'''


def capitalizar_palabras(cadena:str):
    cadena_capitalizada = ""
    cadena = cadena.split()
    for palabra in cadena:
        cadena_capitalizada += palabra.capitalize() + " "

    return cadena_capitalizada

def obtener_nombre_y_dato(lista_heroes:list, nombre:str, key:str):
    for heroe in lista_heroes:
        if heroe['nombre'] == nombre:
            nombre_dato = f"Nombre: {capitalizar_palabras(heroe['nombre'])} | {key}: {heroe[key]} "
            return nombre_dato
